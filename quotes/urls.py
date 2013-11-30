from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import RedirectView


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^quotes/', include('webapp.urls', namespace='webapp')),
    url(r'^$', RedirectView.as_view(url='quotes'), name='home'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('allauth.urls')),
)
