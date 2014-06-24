=========
IconFonts
=========

.. image:: https://badge.fury.io/py/IconFonts.png
    :target: https://badge.fury.io/py/IconFonts

.. image:: https://travis-ci.org/joke2k/iconfonts.png?branch=master
    :target: https://travis-ci.org/joke2k/iconfonts

.. image:: https://coveralls.io/repos/joke2k/iconfonts/badge.png?branch=master
    :target: https://coveralls.io/r/joke2k/iconfonts?branch=master

This package provides a toolkit to render icon-font glyphs.

Documentation
-------------

The full documentation is at https://iconfonts.readthedocs.org.

Quickstart
----------

Install IconFonts::

    pip install iconfonts

Then use it in a project::

    >>> import iconfonts
    >>> iconfonts.get_icon('star')
    u'<i class="star"></i>'

Features
--------

* Multiple Icon font supported
* Auto registration of IconFonts
* Third party template systems integration (django)
* Tests

Installed Fonts
---------------

* `Font-Awesome`_ (font-awesome or fa)
* `Ionicons`_ (ionicons or ion)
* `Open Iconic`_ (iconic or oi)
* `Glyphicon`_ (glyph-icons or glyph)
* `DashIcons`_ (dash-icons or dash)
* `Foundation Icons`_ (foundation or fo)
* `Flag Icons`_ (flag-icons or flags)
* `Wheather Icons`_ (weather-icons or weather)

.. _Font-Awesome: http://fontawesome.io/
.. _Ionicons: http://ionicons.com/
.. _Open Iconic: http://useiconic.com/open/
.. _Glyphicon: http://glyphicons.com/
.. _DashIcons: http://melchoyce.github.io/dashicons/
.. _Foundation Icons: http://zurb.com/playground/foundation-icon-fonts-3
.. _Flag Icons: http://lipis.github.io/flag-icon-css/
.. _Wheather Icons: http://erikflowers.github.io/weather-icons/
