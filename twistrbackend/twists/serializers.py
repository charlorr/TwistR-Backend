from rest_framework import serializers
from .models import Twist, Like

class TwistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Twist
<<<<<<< HEAD
        fields = ('pk', 'user', 'author', 'tag')

class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = ('pk', 'user', 'post')
=======
        fields = ('pk', 'user', 'author', 'tag', 'followed')
>>>>>>> seen-tags
