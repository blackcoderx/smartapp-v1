from rest_framework import serializers

from .models import *


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['host'] = user
        return super().create(validated_data)


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
