from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import *
from .serializers import ActivitySerializer

class ActivityList(generics.ListCreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    permission_classes = (IsAuthenticatedOrReadOnly, )
    authentication_classes = (JSONWebTokenAuthentication, )

    #def get_queryset(self):
    #    user = self.request.user
    #    return user.follows.all()
