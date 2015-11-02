from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import *



class FollowerList(generics.ListCreateAPIView):
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer

    #permission_classes = (IsAuthenticatedOrReadOnly, )
    #authentication_classes = (JSONWebTokenAuthentication, )

    def get_queryset(self):
        user = self.request.user

        if user.is_authenticated():
            return user.follow.all()
        else:
            return Follower.objects.all()

class FollowerDetail(generics.RetrieveDestroyAPIView):
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer

    permission_classes = (IsAuthenticatedOrReadOnly, )
    authentication_classes = (JSONWebTokenAuthentication, )
