from django.conf.urls import patterns, include, url
from settings import MEDIA_ROOT

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django_conventions import UrlsManager
import science_combinator.views as root

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sciencecombinator.views.home', name='home'),
    # url(r'^sciencecombinator/', include('sciencecombinator.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT, 'show_indexes': True}),
)

UrlsManager(urlpatterns, root)