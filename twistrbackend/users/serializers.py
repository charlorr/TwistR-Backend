from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('pk', 'username', 'email', 'phone_number', 'first_name', 'last_name', 'password', 'bio', 'joined_date')
