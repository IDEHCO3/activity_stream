from django.conf.urls import patterns, url
from .views import *

urlpatterns = patterns('',
    url(r'^$', ActivityList.as_view(), name='list'),
)