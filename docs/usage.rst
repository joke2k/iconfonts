=====
Usage
=====

To use IconFonts in a project::

    >>> import iconfonts
    >>> iconfonts.get_font('font-awesome').render_icon('star')
    u'<i class="fa fa-star"></i>'


Django intergration
-------------------

Template tags::

    {% font_stylesheet %}
    {% icon 'star' title='FontAwesome star'%}

    {% font_stylesheet 'iconic' %}
    {% icon 'star' font='iconic' title='Open-Iconic icon' %}

    {% font_stylesheet 'ionicons' %}
    {% icon 'star' font='ionicons' title='Ionicons icon' %}

    {% font_stylesheet 'glyph' %}
    {% icon 'star' font='glyph' title='Glyphicons icon' %}

    {% font_stylesheet 'dash' %}
    {% icon 'star-filled' font='dash' title='Dashicons icon' %}

    {% font_stylesheet 'foundation' %}
    {% icon 'star' font='foundation' title='Foundation icon' %}

    {% font_stylesheet 'weather' %}
    {% icon 'day-sunny' font='weather' title='Weather icon' %}

    {% font_stylesheet 'flags' %}
    {% icon 'it' font='flags' title='FlagIcons icon' %}


Setup `ICONFONT='font-awesome'` variable in your settings then you can omit the font.

Custom fonts
~~~~~~~~~~~~

`iconfonts.django` application auto-loads all `<app>.fonts` modules from `settings.INSTALLED_APPS`.