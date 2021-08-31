import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckan.lib.plugins import DefaultTranslation

from ckanext.depositar_theme import helpers


class Depositar_ThemePlugin(plugins.SingletonPlugin, DefaultTranslation):
    plugins.implements(plugins.ITranslation)
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)
    plugins.implements(plugins.IRoutes, inherit=True)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'fanstatic')
        toolkit.add_resource('fanstatic', 'depositar_theme')

    # ITemplateHelpers

    def get_helpers(self):
        function_names = (
            'get_legal_versions',
            'get_latest_legal_version',
        )
        return _get_module_functions(helpers, function_names)

    # IRoutes

    def before_map(self, map):
        legal_controller = 'ckanext.depositar_theme.controllers.legal:LegalController'

        map.connect('terms_of_use', '/terms_of_use',
            controller=legal_controller, action='tou')

        map.connect('tou_archive', '/terms_of_use/archive',
            controller=legal_controller, action='tou_archive')

        map.connect('archived_tou', '/terms_of_use/archive/{version}',
            controller=legal_controller, action='tou')

        map.connect('privacy', '/privacy',
            controller=legal_controller, action='privacy')

        map.connect('privacy_archive', '/privacy/archive',
            controller=legal_controller, action='privacy_archive')

        map.connect('archived_privacy', '/privacy/archive/{version}',
            controller=legal_controller, action='privacy')

        return map

def _get_module_functions(module, function_names):
    functions = {}
    for f in function_names:
        functions[f] = module.__dict__[f]

    return functions
