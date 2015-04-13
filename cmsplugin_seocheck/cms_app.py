# -*- coding: utf-8 -*-

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


class SeoApp(CMSApp):
    name = 'SeoCheck'
    urls = ['cmsplugin_seocheck.urls', ]
    app_name = 'cmsplugin_seocheck'

apphook_pool.register(SeoApp)
