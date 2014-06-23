from django import template
from iconfonts.api import render_icon, get_font
from iconfonts.django.models import ICONFONT

register = template.Library()


@register.simple_tag
def font_stylesheet(font=ICONFONT):
    return get_font(font).render_stylesheet()

@register.simple_tag
def icon(name, font=ICONFONT, classes='', **attributes):
    return render_icon(name, font, classes=classes, attributes=attributes)

