from django.test.utils import override_settings
from cms.test_utils.testcases import CMSTestCase
from django.test import TestCase, RequestFactory
from django.core.urlresolvers import reverse

from cms.api import create_page, create_title
from cms.middleware.toolbar import ToolbarMiddleware
from cms.toolbar.toolbar import CMSToolbar
from cms.toolbar.items import ModalItem

from djangocms_helper.utils import create_user


class SEOViewTest(CMSTestCase):

    def get_request(self):
        page = create_page(u'page one', 'fullwidth.html', language='en')
        page.publish('en')

        path = page.get_absolute_url()

        admin_user = create_user(
            'admin',
            'admin@admin.com',
            'admin',
            is_staff=True,
            is_superuser=True
        )

        request = RequestFactory().get(path)
        request.current_page = page
        request.user = admin_user
        request.session = {}

        mid = ToolbarMiddleware()
        mid.process_request(request)
        return request

    @override_settings(ROOT_URLCONF='cmsplugin_seocheck.tests.urls')
    def test_get(self):
        response = self.client.get('/en/originalseourl/')
        self.assertEqual(response.status_code, 200)

    @override_settings(ROOT_URLCONF='cmsplugin_seocheck.tests.urls')
    def test_toolbar(self):
        urls = 'cmsplugin_seocheck.tests.urls'
        request = self.get_request()
        toolbar = CMSToolbar(request)
        toolbar.get_left_items()
        seo_menu = toolbar.menus['seo_check']
        self.assertEqual(len(seo_menu.items), 1)
        self.assertEqual(len(seo_menu.find_items(ModalItem, url=reverse('cmsplugin_seocheck:check_modal'))), 1)
