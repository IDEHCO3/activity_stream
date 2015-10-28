from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Activity

class UserActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', 'last_name')
        read_only_fields = ('first_name', 'last_name')

class ActivitySerializer(serializers.ModelSerializer):
    author = UserActivitySerializer(read_only=True)

    class Meta:
        model = Activity
        fields = ('author', 'action', 'url', 'creation_date')


    def create(self, validated_data):
        user = self.context['request'].user
        return Activity.objects.create(user=user, **validated_data)