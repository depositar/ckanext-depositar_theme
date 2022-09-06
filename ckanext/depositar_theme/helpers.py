import os
import inspect

from ckan.common import config
from ckan.lib import mailer
import ckan.lib.base as base
from ckan.lib.base import render
import ckan.lib.helpers as h
from ckan.lib.mailer import create_reset_key, get_reset_link, mail_user
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

def get_format_count():
    results = tk.get_action('package_search')({}, {})['results']
    format_list = []
    for res in results:
        resource_list = res['resources']
        for resource in resource_list:
            format_list.append(resource['format'].upper())

    format_count = dict((fmt, format_list.count(fmt)) for fmt in format_list)
    if '' in format_count:
        format_count.pop('')
    sort_format_count = sorted(format_count.items(), key=lambda tup: tup[1], reverse=True)
    return sort_format_count

def get_total_views():
    package_list = tk.get_action('package_list')({},{})
    total_views = 0
    for pkg in package_list:
        data = {'id': pkg, 'include_tracking': True}
        pkg_content = tk.get_action('package_show')({}, data)
        if(pkg_content['type'] == 'dataset'):
            total_views += pkg_content['tracking_summary']['total']
    return h.SI_number_span(total_views)

def get_showcase():
    showcase_list = tk.get_action('ckanext_showcase_list')({}, {})
    case_list = []
    for showcase in showcase_list:
        case_list.append({
            'title': showcase['title'],
            'href': showcase['name'],
            'content': h.render_markdown(showcase['notes']),
            'image_url': showcase['extras'][0]['value']
        })
    return case_list

def get_markdown(content):
    return h.render_markdown(content)