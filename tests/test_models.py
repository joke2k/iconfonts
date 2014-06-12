#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
test_iconfonts
------------

Tests for `iconfonts` models module.
"""
import unittest
from functools import partial
from django.conf import settings
from django.template import Context, Template
from iconfonts import api
from iconfonts import utils

_ = utils.string

class TestIconfonts(unittest.TestCase):

    class MyFont(api.IconsFont):
        name = 'my-font'
        shortcut = 'my'
        css_url = '//mysite.com/css/font.css'

    def test_auto_registration(self):

        self.assertIn(self.MyFont, api.IconsFont.registry)

    def test_get_font(self):

        font = api.get_font('my-font')
        self.assertIsInstance(font, self.MyFont)

    def test_get_font_by_shortcut(self):

        font = api.get_font('my')
        self.assertIsInstance(font, self.MyFont)

    def _render_icon(self, renderer):
        self.assertEqual(renderer('star'), _('<i class="star"></i>'))
        self.assertEqual(renderer('star', tag='span'), _('<span class="star"></span>'))
        self.assertEqual(renderer('star', attributes={'title': 'My title'}), _('<i class="star" title="My title"></i>'))
        self.assertEqual(renderer('star', classes='small'), _('<i class="small star"></i>'))

    def test_render_icon(self):

        font = api.get_font('my-font')
        self._render_icon(font.render_icon)

        self._render_icon(partial(api.render_icon, font='my-font'))

    def test_render_stylesheet_loader(self):

        result = _('<link href="{url}" rel="stylesheet">').format(url=self.MyFont.css_url)

        font = api.get_font('my-font')
        self.assertEqual(font.render_stylesheet(), result)

        self.assertEqual(api.render_stylesheet('my-font'), result)


class TestDjangoIntegration(unittest.TestCase):

    def render_template(self, template, context=None):
        t = Template(template)
        c = Context(context or {})
        return t.render(c)

    def test_icon_tag(self):
        rendered = self.render_template("{% load icons %}{% icon 'star' font='ionicons' %}")
        self.assertEqual(rendered,_('<i class="icon ion-star"></i>'))

    def test_icon_tag_from_settings(self):
        self.assertEqual(settings.ICONFONT, 'font-awesome')
        rendered = self.render_template("{% load icons %}{% icon 'star' %}")
        self.assertEqual(rendered,_('<i class="fa fa-star"></i>'))
