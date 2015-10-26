from rest_framework import generics
from .models import *


class ActivityList(generics.ListCreateAPIView):
    queryset = Activity.objects.all()
