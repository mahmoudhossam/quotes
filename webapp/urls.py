from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
    url(r'^(?P<pk>\d)/$', views.ViewQuote.as_view(), name='view_single'),
    url(r'^add$', views.AddQuote.as_view(), name='add'),
    url(r'^$', views.QuoteList.as_view(), name='view_all'),
)
