import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckan.lib.plugins import DefaultTranslation

from ckanext.depositar_theme import helpers, routes
from ckanext.depositar_theme.cli import get_commands


class DepositarThemeRepStr(plugins.SingletonPlugin, DefaultTranslation):

    plugins.implements(plugins.ITranslation)

    # ITranslation
    def i18n_domain(self):
        return 'rep_str'

class Depositar_ThemePlugin(plugins.SingletonPlugin, DefaultTranslation):
    plugins.implements(plugins.ITranslation)
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)
    plugins.implements(plugins.IBlueprint, inherit=True)
    plugins.implements(plugins.IClick)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'fanstatic')
        toolkit.add_resource('fanstatic', 'depositar_theme')

    # ITemplateHelpers

    def get_helpers(self):
        function_names = (
            'get_doc_url',
            'get_legal_versions',
            'get_latest_legal_version',
            'get_format_count',
            'get_total_views',
            'get_showcase',
            'get_markdown'
        )
        return _get_module_functions(helpers, function_names)

    # IBlueprint

    def get_blueprint(self):
        return routes.blueprints

    # IClick

    def get_commands(self):
        return get_commands()

def _get_module_functions(module, function_names):
    functions = {}
    for f in function_names:
        functions[f] = module.__dict__[f]

    return functions