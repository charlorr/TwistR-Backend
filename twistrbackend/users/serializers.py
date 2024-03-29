from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User

class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],
                                        validated_data['email'],
                                        validated_data['password'],
                                        first_name = validated_data['first_name'],
                                        last_name = validated_data['last_name'],
                                        bio = validated_data['bio'],
                                        phone_number = validated_data['phone_number'])
        return user
    class Meta:
        model = User
        fields = ('pk', 'username', 'email', 'phone_number', 'first_name', 'last_name', 'password', 'bio', 'theme', 'joined_date')


class LoginUserSerializer (serializers.Serializer):
    #user name is actually email. confused as to why but okay will fix soon
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
            # ** unpacks the data into authenticate w/ dictiionary key-value pairs
            print("This is what coming")
            print(data)
            user = authenticate(**data)
            if user and user.is_active:
                print("This is what coming2")
                return user
            else:
                try:
                    try_user = User.objects.get(username=data.get('username'))
                    print(try_user.email)
                    data["username"] = try_user.email
                    user = authenticate(**data)
                    if user and user.is_active:
                        return user
                except User.DoesNotExist:
                    raise serializers.ValidationError("Unable to login with credentials")
