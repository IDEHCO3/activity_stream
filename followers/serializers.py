from rest_framework import serializers
from .models import Follower

class FollowerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Follower

    def create(self, validated_data):
        list = Follower.objects.filter(**validated_data)
        if list:
            return list[0]
        else:
            if validated_data['user'].id == validated_data['follow'].id:
                return None
            follower = Follower(**validated_data)
            follower.save()
            return follower
