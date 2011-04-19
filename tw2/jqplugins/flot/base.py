
import tw2.core as twc
import tw2.jquery.base as twjq_c
import defaults

flot_js = twjq_c.jQueryPluginJSLink(
    name=defaults._flot_name_,
    version=defaults._flot_version_,
    variant='min',
    modname='tw2.jqplugins.flot',
    subdir = '',
)
flot_utils_js = twc.JSLink(
    modname='tw2.jqplugins.flot',
    filename='static/js/flot-utils.js',
)

__all__ = ['flot_js', 'flot_utils_js']
