import ckan.plugins as p
from ckan.common import c, _
from ckan.lib.jinja_extensions import TemplateNotFound

from ckanext.depositar_theme.lib import jinja_extensions


class LegalController(p.toolkit.BaseController):

    def tou(self, version=None):
        c.pylons.app_globals.jinja_env.filters['localized_date'] = \
                jinja_extensions.localized_date
        try:
            return p.toolkit.render('legal/tou.html', \
                    {'title': _('Terms of Use'), 'version': version})
        except TemplateNotFound as e:
            base.abort(404)

    def tou_archive(self):
        return p.toolkit.render('legal/tou_archive.html', \
                {'title': _('Terms of Use (Archive)')})

    def privacy(self, version=None):
        c.pylons.app_globals.jinja_env.filters['localized_date'] = \
                jinja_extensions.localized_date
        try:
            return p.toolkit.render('legal/privacy.html', \
                    {'title': _('Privacy Policy'), 'version': version})
        except TemplateNotFound as e:
            base.abort(404)

    def privacy_archive(self):
        return p.toolkit.render('legal/privacy_archive.html', \
                {'title': _('Privacy Policy (Archive)')})
