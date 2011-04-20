
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

__all__ = ['flot_js']
