from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'pitanja.views.unos', name='unos'),
    url(r'^question$', 'pitanja.views.question', name='question'),
    url(r'^question/(?P<redni_broj>\d+)$', 'pitanja.views.question', name='question'),
    # url(r'^pitanja/', include('pitanja.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
