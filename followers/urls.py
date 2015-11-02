from django.conf.urls import patterns, url

from .views import *

urlpatterns = patterns('',
    url(r'^$', FollowerList.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', FollowerDetail.as_view(), name='detail')
)