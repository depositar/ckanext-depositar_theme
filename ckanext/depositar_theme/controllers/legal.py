import ckan.plugins as p
from ckan.common import c, _

from ckanext.depositar_theme import helpers
from ckanext.depositar_theme.lib import jinja_extensions


class LegalController(p.toolkit.BaseController):

    def tou(self, version=helpers.get_latest_legal_version('tou')):
        c.pylons.app_globals.jinja_env.filters['localized_date'] = \
                jinja_extensions.localized_date
        text = helpers.get_legal('tou', version)
        return p.toolkit.render('legal/tou.html', \
                {'title': _('Terms of Use'), 'version': version,
                 'text': text})

    def tou_archive(self):
        return p.toolkit.render('legal/tou_archive.html', \
                {'title': _('Terms of Use (Archive)')})

    def privacy(self, version=helpers.get_latest_legal_version('privacy')):
        c.pylons.app_globals.jinja_env.filters['localized_date'] = \
                jinja_extensions.localized_date
        text = helpers.get_legal('privacy', version)
        return p.toolkit.render('legal/privacy.html', \
                {'title': _('Privacy Policy'), 'version': version,
                 'text': text})

    def privacy_archive(self):
        return p.toolkit.render('legal/privacy_archive.html', \
                {'title': _('Privacy Policy (Archive)')})
