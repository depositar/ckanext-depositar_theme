import os
import inspect

from ckan.common import config
from ckan.lib import mailer
from ckan.lib.base import render_jinja2
from ckan.lib.mailer import create_reset_key, get_reset_link, mail_user

from ckanext import depositar_theme


def get_legal_versions(folder):
    p = os.path.join(os.path.dirname( \
            inspect.getfile(depositar_theme)), \
            'templates', 'legal', folder)
    files_no_ext = [''.join(f.split('.')[:-1]) \
            for f in sorted(os.listdir(p), reverse=True)]

    return files_no_ext

def get_latest_legal_version(folder):

    return get_legal_versions(folder)[0]

def get_reg_link_body(user):
    extra_vars = {
        'reg_link': get_reset_link(user),
        'site_title': config.get('ckan.site_title'),
        'site_url': config.get('ckan.site_url'),
        'user_name': user.name,
        'tos_version': get_latest_legal_version('tos'),
        'privacy_version': get_latest_legal_version('privacy')
        }
    return render_jinja2('emails/user_registration.txt', extra_vars)

def send_reg_link(user):
    create_reset_key(user)
    body = get_reg_link_body(user)
    extra_vars = {
        'site_title': config.get('ckan.site_title'),
    }
    subject = render_jinja2('emails/user_registration_subject.txt', extra_vars)

    # Make sure we only use the first line
    subject = subject.split('\n')[0]

    mail_user(user, subject, body)
