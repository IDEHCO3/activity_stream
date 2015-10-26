from django.conf.urls import url
from .views import *

urlpatterns = ('',
               url(r'^$', ActivityList.as_view(), name='list')
)