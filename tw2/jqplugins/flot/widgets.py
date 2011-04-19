from tw2.core.resources import encoder
import tw2.core as twc
import tw2.jquery
import tw2.excanvas
import base
import tw2.jqplugins.ui.base as tw2_jq_ui

class FlotWidget(tw2_jq_ui.JQueryUIWidget):
    resources = [tw2.jquery.jquery_js,
                 base.flot_js,
                 tw2.excanvas.excanvas_js
                ]
    template = "mako:tw2.jqplugins.flot.templates.flot"

    data = twc.Param("An array of data series", default=[])
    options = twc.Param("Plot options", default={}) 
    height = twc.Param("The height of the graph", default='300px',
                       attribute=True)
    width = twc.Param("The width of the graph", default='600px',
                      attribute=True)
    label = twc.Param("Label for the graph", default='',)

    def prepare(self):
        self._data = encoder.encode(self.data)
        self._options = encoder.encode(self.options)
        super(FlotWidget, self).prepare()
