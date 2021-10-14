from flask import Blueprint, current_app

from ckan.common import _
from ckan.plugins import toolkit

from ckanext.depositar_theme import helpers
from ckanext.depositar_theme.lib import jinja_extensions

blueprint = Blueprint(name='legal', import_name=__name__)


@blueprint.before_app_first_request
def init_jinja_extensions():
    current_app.jinja_env.filters['localized_date'] = \
        jinja_extensions.localized_date

@blueprint.route('/terms_of_use')
@blueprint.route('/terms_of_use/archive/<version>')
def tou(version=helpers.get_latest_legal_version('tou')):
    text = helpers.get_legal('tou', version)
    return toolkit.render('legal/tou.html', {
        'title': _('Terms of Use'), 'version': version, 'text': text
    })

@blueprint.route('/terms_of_use/archive')
def tou_archive():
    return toolkit.render('legal/tou_archive.html', {
        'title': _('Terms of Use (Archive)')})

@blueprint.route('/privacy')
@blueprint.route('/privacy/archive/<version>')
def privacy(version=helpers.get_latest_legal_version('privacy')):
    text = helpers.get_legal('privacy', version)
    return toolkit.render('legal/privacy.html', {
        'title': _('Privacy Policy'), 'version': version, 'text': text
    })

@blueprint.route('/privacy/archive')
def privacy_archive():
    return toolkit.render('legal/privacy_archive.html', {
        'title': _('Privacy Policy (Archive)')})
