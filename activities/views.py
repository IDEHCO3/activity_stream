from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.db.models import Q
from datetime import datetime, timedelta
from .models import *
from .serializers import ActivitySerializer

class ActivityList(generics.ListCreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    permission_classes = (IsAuthenticatedOrReadOnly, )
    authentication_classes = (JSONWebTokenAuthentication, )

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated():
            condition = Q(author__id=user.id)
            for follower in user.follow.all():
                condition = condition | Q(author__id=follower.follow.id)
            return Activity.objects.filter(condition)
        else:
            return Activity.objects.all()

class ActivityRecentlyList(generics.ListAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    permission_classes = (IsAuthenticatedOrReadOnly, )
    authentication_classes = (JSONWebTokenAuthentication, )

    def get_queryset(self):
        user = self.request.user

        timerestriction = 1
        now = datetime.now()
        delta = timedelta(hours=timerestriction)
        time = now - delta
        condition = Q(creation_date__gte=time)

        if user.is_authenticated():
            condition = condition & Q(author__id=user.id)
            for follower in user.follow.all():
                condition = condition | Q(author__id=follower.follow.id)

        return Activity.objects.filter(condition)
