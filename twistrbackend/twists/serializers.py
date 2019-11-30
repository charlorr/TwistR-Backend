from rest_framework import serializers
from .models import Twist, Like

class TwistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Twist
        fields = ('pk', 'user', 'author', 'tag', 'followed')

class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = ('pk', 'user', 'post')
