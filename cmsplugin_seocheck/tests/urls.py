from django.conf.urls.i18n import i18n_patterns
from django.conf.urls import patterns, include, url

urlpatterns += i18n_patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('djangocms_blog.urls', namespace='djangocms_blog')),
    url(r'^', include('cms.urls')),
)
