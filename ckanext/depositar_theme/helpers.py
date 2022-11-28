import os
import inspect

from ckan.common import config
from ckan.lib import mailer
import ckan.lib.base as base
from ckan.lib.base import render
import ckan.lib.helpers as h
from ckan.lib.mailer import create_reset_key, get_reset_link, mail_user
import ckan.model as model
import ckantoolkit as tk

from ckanext import depositar_theme
from ckanext.data_depositario import helpers as depositar_helpers


def get_doc_url():
    lang = 'zh_TW' if h.lang() == 'zh_Hant_TW' else h.lang()
    return 'https://docs.depositar.io/{0}/{1}/'.format( \
            lang, depositar_helpers.get_pkg_version())

def get_legal_path(_type):
    return os.path.join(os.path.dirname( \
            inspect.getfile(depositar_theme)), \
            'templates', 'legal', _type)

def get_legal_versions(_type):
    return sorted(os.listdir(get_legal_path(_type)), reverse=True)

def get_latest_legal_version(_type):
    return get_legal_versions(_type)[0]

def get_legal(_type, version, lang=None):
    if not lang: lang = h.lang()
    path = os.path.join(get_legal_path(_type), version,
                        '{lang}.md'.format(lang=lang))
    try:
        with open(path) as f:
            formatted = h.render_markdown(f.read(), allow_html=True)
            f.close()
            return formatted
    except IOError as e:
        if version in get_legal_versions(_type):
            # Fallback to English
            return get_legal(_type, version, 'en')
        else:
            base.abort(404)

def get_reg_link_body(user):
    extra_vars = {
        'reg_link': get_reset_link(user),
        'site_title': config.get('ckan.site_title'),
        'site_url': config.get('ckan.site_url') + '/' + h.lang(),
        'user_name': user.name,
        'tou_version': get_latest_legal_version('tou'),
        'privacy_version': get_latest_legal_version('privacy')
        }
    return render('emails/user_registration.txt', extra_vars)

def send_reg_link(user):
    create_reset_key(user)
    body = get_reg_link_body(user)
    extra_vars = {
        'site_title': config.get('ckan.site_title'),
    }
    subject = render('emails/user_registration_subject.txt', extra_vars)

    # Make sure we only use the first line
    subject = subject.split('\n')[0]

    mail_user(user, subject, body)

def get_total_views():
    sql = """
        SELECT SUM(t.total_views) FROM (
            SELECT COALESCE(SUM(s.count), 0) AS total_views
            FROM package AS p
            LEFT OUTER JOIN tracking_summary AS s ON s.package_id = p.id
            WHERE p.private = 'false' AND p.state = 'active'
            ORDER BY total_views DESC) t
    """

    engine = model.meta.engine
    total_views = engine.execute(sql).fetchone()[0]

    return h.SI_number_span(total_views)

def get_showcases():
    showcases = tk.get_action('package_search')(
        {},
        {'fq': 'dataset_type:showcase'})['results']

    for showcase in showcases:
        # Borrowed from ckanext-showcase
        image_url = showcase.get('image_url')
        showcase['image_display_url'] = image_url
        if image_url and not image_url.startswith('http'):
            showcase['image_url'] = image_url
            showcase['image_display_url'] = \
                h.url_for_static('uploads/{0}/{1}'
                                 .format('showcase',
                                         showcase.get('image_url')),
                                 qualified=True)

    return showcases

def get_markdown(content):
    return h.render_markdown(content)
