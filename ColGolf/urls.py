from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    url(r'^$', 'website.views.home', name='home'),
    url(r'^accounts/profile/$', 'website.views.home', name='another home'),
    url(r'^city/fauna$', 'website.views.fauna', name='fauna'),
    url(r'^city/flora$', 'website.views.flora', name='flora'),
    url(r'^city$', 'website.views.city', name='city'),
    url(r'^campo$', 'website.views.campo', name='campo'),
    url(r'^club$', 'website.views.club', name='club'),
    url(r'^region$', 'website.views.region', name='region'),
    # url(r'^ColGolf/', include('ColGolf.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'admin/login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
    url(r'^admin/', include(admin.site.urls)),
)
