from django.conf.urls import patterns, include, url
import webapp.views
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'quotes.views.home', name='home'),
    # url(r'^quotes/', include('quotes.foo.urls')),
    url(r'^quotes/(?P<pk>\d)/$', webapp.views.ViewQuote.as_view()),
    url(r'^quotes/add$', webapp.views.AddQuote.as_view()),
    url(r'^$', webapp.views.QuoteList.as_view()),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

)
