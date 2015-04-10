from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.subject),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.detail),
    url(r'^about/$', views.about),

)