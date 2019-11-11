from rest_framework import serializers
from .models import Twist

class TwistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Twist
        fields = ('pk', 'user', 'author', 'tag')
