import os
import inspect

from ckan.common import config
from ckan.lib import mailer
from ckan.lib.base import render_jinja2

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
