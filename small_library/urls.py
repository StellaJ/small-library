#-*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'libraries.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^small_library_app/', include('small_library_app.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^desc/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,  'show_indexes': True, }),
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes': True, }),
    )
