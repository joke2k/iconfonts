# -*- coding: utf-8 -*-
from iconfonts import utils

string = utils.string

class IconsFont(object):

    __metaclass__ = utils.RegisterLeafClasses

    name = ''
    shortcut = ''
    css_url = ''
    tag = 'i'
    tag_classes = ''
    tag_attributes = {}
    prefix = ''

    registry = set()

    def __init__(self):
        if not self.name:
            raise NotImplementedError

    def render_stylesheet(self):
        return string('<link href="{url}" rel="stylesheet">').format(url=self.css_url)

    def render_icon(self, name, classes=string(''), attributes=None, tag=None):
        attributes = self.build_attributes(attributes)
        attributes['class'] = self.build_classes(self.tag_classes, attributes.get('class', None), classes)
        return self.build_element(tag or self.tag, name, attributes)

    def build_attributes(self, attributes):
        attrs = self.tag_attributes.copy()
        if attributes:
            attrs.update(attributes)
        return attrs

    def build_classes(self, *classes):
        class_set = []
        for item in classes:
            if not item:
                # skip empty/none items
                continue
            # split if it is a string
            if isinstance(item, utils.string_types):
                item = item.split(' ')
            # then add to class set
            class_set += item
        # join all together with spaces
        return string(' ').join(set(sorted(class_set)))

    def add_name_to_attributes(self, name, attributes):
        # add prefix if not already added
        if not name.startswith(self.prefix):
            name = string('').join([self.prefix, name])

        # add real name to classes
        attributes['class'] = string(' ').join([attributes['class'], name]).strip()

    def build_element(self, tag, name, attributes):

        self.add_name_to_attributes(name, attributes)

        # prepare element html to render the font icon
        return string('<{tag}{attributes}></{tag}>').format(
            tag=tag,
            attributes=utils.flatatt(attributes),
        )

class FontAwesomeFont(IconsFont):
    """
    http://fontawesome.io/icons/
    <i class="fa fa-star"></i>
    """
    name = 'font-awesome'
    shortcut = 'fa'
    css_url = '//cdn.jsdelivr.net/fontawesome/latest/css/font-awesome.css'
    tag_classes = 'fa'
    prefix = 'fa-'


class IoniconsFont(IconsFont):
    """
    http://ionicons.com/
    <i class="icon ion-star"></i>
    """
    name = 'ionicons'
    shortcut = 'ion'
    css_url = '//cdn.jsdelivr.net/ionicons/latest/css/ionicons.css'
    tag_classes = 'icon'
    prefix = 'ion-'

class OpenIconicFont(IconsFont):
    """
    https://useiconic.com/open/
    <i class="oi" data-glyph="star"></i>
    """
    name = 'iconic'
    shortcut = 'oi'
    css_url = '//cdn.jsdelivr.net/open-iconic/latest/font/css/open-iconic.css'
    tag_classes = 'oi'
    prefix = 'oi-'

    def add_name_to_attributes(self, name, attributes):
        """
        data-glyph="icon-name"
        """
        attributes['data-glyph'] = name

class GlyphIconsFont(IconsFont):
    """
    http://glyphicons.com/
    <i class="glyphicon glyphicon-star"></i>
    """
    name = 'glyph-icons'
    shortcut = 'glyph'
    css_url = '//netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap-glyphicons.css'
    tag_classes = 'glyphicon'
    prefix = 'glyphicon-'


class DashIconsFont(IconsFont):
    """
    http://melchoyce.github.io/dashicons/
    <i class="dashicons dashicons-star-filled"></i>
    """
    name = 'dash-icons'
    shortcut = 'dash'
    css_url= '//cdn.jsdelivr.net/dashicons/latest/css/dashicons.min.css'
    tag_classes = 'dashicons'
    prefix = 'dashicons-'

class FoundationIconsFont(IconsFont):
    """
    http://zurb.com/playground/foundation-icon-fonts-3
    <i class="fi-heart"></i>
    """
    name = 'foundation'
    shortcut = 'fo'
    css_url = '//cdnjs.cloudflare.com/ajax/libs/foundicons/3.0.0/foundation-icons.css'
    prefix = 'fi-'

class FlagIconsFont(IconsFont):
    """
    http://lipis.github.io/flag-icon-css/
    <span class="flag-icon flag-icon-it"></span>
    """
    name = 'flag-icons'
    shortcut = 'flags'
    css_url = '//cdn.jsdelivr.net/flag-icon-css/latest/css/flag-icon.css'
    tag = 'span'
    tag_classes = 'flag-icon'
    prefix = 'flag-icon-'

class WheatherIconsFont(IconsFont):
    """
    http://erikflowers.github.io/weather-icons/
    <i class="wi wi-day-lightning"></i>
    """
    name = 'weather-icons'
    shortcut = 'weather'
    css_url = '//cdn.jsdelivr.net/weather-icons/latest/css/weather-icons.min.css'
    tag_classes = 'wi'
    prefix = 'wi-'
