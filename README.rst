tw2.jqplugins.flot
=========================

:Author: Ralph Bean <rbean@redhat.com>

.. comment: split here

.. _toscawidgets2 (tw2): http://toscawidgets.org/documentation/tw2.core/
.. _flot: http://code.google.com/p/flot/

tw2.jqplugins.flot is a `toscawidgets2 (tw2)`_ wrapper for `flot`_.

Live Demo
---------
Peep the `live demonstration <http://tw2-demos.threebean.org/module?module=tw2.jqplugins.flot>`_.

Links
-----
Get the `source from github <http://github.com/toscawidgets/tw2.jqplugins.flot>`_.

`PyPI page <http://pypi.python.org/pypi/tw2.jqplugins.flot>`_
and `bugs <http://github.com/toscawidgets/tw2.jqplugins.flot/issues/>`_

Description
-----------

`toscawidgets2 (tw2)`_ aims to be a practical and useful widgets framework
that helps people build interactive websites with compelling features, faster
and easier. Widgets are re-usable web components that can include a template,
server-side code and JavaScripts/CSS resources. The library aims to be:
flexible, reliable, documented, performant, and as simple as possible.

`flot`_ is a pure Javascript plotting library for jQuery. It produces graphical
plots of arbitrary datasets on-the-fly client-side.

This module, tw2.jqplugins.flot, provides `toscawidgets2 (tw2)`_ access
to `flot`_ widgets.

Sampling tw2.jqplugins.flot in the WidgetBrowser
------------------------------------------------

The best way to scope out ``tw2.jqplugins.flot`` is to load its widgets in the
``tw2.devtools`` WidgetBrowser.  To see the source code that configures them,
check out ``tw2.jqplugins.flot/tw2/jqplugins/flot/samples.py``

To give it a try you'll need git, python, and `virtualenvwrapper
<http://pypi.python.org/pypi/virtualenvwrapper>`_.  Run::

    $ git clone git://github.com/toscawidgets/tw2.jqplugins.flot.git
    $ cd tw2.jqplugins.flot
    $ mkvirtualenv tw2.jqplugins.flot
    (tw2.jqplugins.flot) $ pip install tw2.devtools
    (tw2.jqplugins.flot) $ python setup.py develop
    (tw2.jqplugins.flot) $ paster tw2.browser

...and browse to http://localhost:8000/ to check it out.
