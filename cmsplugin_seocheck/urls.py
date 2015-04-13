# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from .views import SeoCheckView

urlpatterns = patterns(
    '',
    url(r'^$', SeoCheckView.as_view(), name="check_modal"),
)
