
import tw2.core as twc
import tw2.jquery
import defaults

flot_js = twc.JSLink(
    modname=__name__,
    filename='static/jqplugins/flot/0.7/jquery.flot.min.js',
    resources = [tw2.jquery.jquery_js],
)

__all__ = ['flot_js']
