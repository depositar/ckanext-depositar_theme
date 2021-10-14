from flask import Blueprint

from ckan.common import _
from ckan.plugins import toolkit

blueprint = Blueprint(name='help', import_name=__name__, url_prefix='/help')


@blueprint.route('/')
@blueprint.route('')
def index():
    '''Render the help index.'''
    return toolkit.render('help/index.html', {
        'title': _('Help')
    })
