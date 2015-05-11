from django.conf.urls.i18n import i18n_patterns
from django.conf.urls import patterns, include, url

from django.contrib import admin

urlpatterns = i18n_patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^originalseourl/', include('cmsplugin_seocheck.urls', namespace="cmsplugin_seocheck")),
    url(r'^', include('cms.urls')),
)
