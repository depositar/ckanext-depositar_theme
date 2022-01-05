import os
import re
import inspect

import click
import polib
import ckan.plugins.toolkit as tk


ckan_p = os.path.dirname(inspect.getfile(__import__('ckan', fromlist=[''])))
theme_p = os.path.dirname(inspect.getfile(__import__('ckanext.depositar_theme', fromlist=[''])))

@click.group(u'depositar_theme')
def depositar_theme():
    '''Depositar theme commands'''
    pass

@depositar_theme.command(u'replace_po')
def replace_po_cmd():
    replace_po()
    try:
        replace_po()
    except Exception as e:
        tk.error_shout(e)
    else:
        click.secho(u'Done. Please replace extracted strings and compile them with msgfmt.',
                    fg=u'green', bold=True)

def replace_po():
    pot = polib.pofile(os.path.join(ckan_p, 'i18n', 'ckan.pot'))
    out = parse_str(pot)

    out.metadata['Language'] = 'en'
    out.save(os.path.join(theme_p, get_lang_path('en'), 'rep_str.po'))

    out.metadata['Language'] = 'zh_Hant_TW'
    out.save(os.path.join(theme_p, get_lang_path('zh_Hant_TW'), 'rep_str.po'))

def parse_str(po):

    ignore_list = \
        ['ckanext/reclineview/theme/templates/recline_graph_form.html',
        'ckan/templates/home/snippets/about_text.html',
        'ckan/templates/organization/snippets/organization_item.html',
        'ckan/templates/snippets/activities/follow_group.html'
        ]

    out = polib.POFile()
    out.metadata = po.metadata

    for message in po.untranslated_entries():
        if message.occurrences[0][0] in ignore_list:
            continue
        if re.match(r'^(.*[^{]*)[Gg]roup([^}]*.*)$', message.msgid) or \
                re.match(r'^(.*[^{]*)[Oo]rganization([^}]*.*)$', message.msgid):
            out.append(message)

    return out

def get_lang_path(lang):
    return os.path.join('i18n', lang, 'LC_MESSAGES')

def get_commands():
    return [depositar_theme]
