from iconfonts.fonts import IconsFont
from iconfonts.utils import string

def get_font(name=None):
    fonts = [font for font in IconsFont.registry]
    name = name or fonts[0].name
    for font_class in fonts:
        if name not in (font_class.name, font_class.shortcut):
            continue
        return font_class()
    raise NotImplemented("Cannot retrieve a icon font with name '%s'" % name)


def render_icon(name, font=None, classes=string(''), attributes=None, tag=None):
    return get_font(font).render_icon(name, classes=classes, attributes=attributes, tag=tag)

def render_stylesheet(font=None):
    return get_font(font).render_stylesheet()