# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from iconfonts import fonts
from iconfonts.django import utils


for app in settings.INSTALLED_APPS:
    provider_module = app + '.fonts'
    try:
        utils.import_string(provider_module)
    except ImproperlyConfigured:
        pass

INSTALLED_ICONFONTS = [cls for cls in fonts.IconsFont]
ICONFONT = getattr(settings, 'ICONFONT', INSTALLED_ICONFONTS[0].name)