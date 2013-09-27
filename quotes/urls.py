from django.conf.urls import patterns, url
import webapp.views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'quotes.views.home', name='home'),
    # url(r'^quotes/', include('quotes.foo.urls')),
    url(r'^quotes/add$', webapp.views.AddQuote.as_view()),
    url(r'^$', webapp.views.QuoteList.as_view()),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
