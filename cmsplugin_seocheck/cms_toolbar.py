# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool


@toolbar_pool.register
class SeoCheckToolbar(CMSToolbar):

    def populate(self):
        seo_check_menu = self.toolbar.get_or_create_menu(
                'seo_check',
                'SEO'
                )
        url = reverse('seo_check:check_modal')
        seo_check_menu.add_modal_item(name='SEO-Check', url=url)
