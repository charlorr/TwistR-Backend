from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status, permissions
#from rest_framework.authtoken.models import Token
from knox.models import AuthToken

from .models import User
from .serializers import *

#use this if the endpoint does not require authentication
#@permission_classes((AllowAny,))

@api_view(['GET'])
@permission_classes((AllowAny,))
def users_list(request):
    """
 List users, or create a new user.
 """
    if request.method == 'GET':
        data = []

        data = User.objects.all()

        username_param = request.query_params.get('username', None)
        email_param = request.query_params.get('email', None)

        if username_param is not None:
            data = data.filter(username=username_param)

        if email_param is not None:
            data = data.filter(email=email_param)

        serializer =  UserSerializer(data,context={'request': request},many=True)

        return Response({'data': serializer.data  })

@api_view(['GET', 'PUT'])
@permission_classes((AllowAny,))
def users_detail(request, pk):
    """
 Retrieve, update or delete a user by id/pk.
 """
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer =  UserSerializer(user,context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        print("hello")
        serializer =  UserSerializer(user, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes((AllowAny,))
def user_register(request):
    print(request)
    serializer =  UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        print(serializer)
        return Response({
            "user" : serializer.data,
            "token" : AuthToken.objects.create(user)[1]
        })
    return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

@api_view(['POST'])
@permission_classes((AllowAny,))
def user_login(request):
    serializer = LoginUserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data
        print(user.pk)
        return Response({
            "user_pk" : user.pk,
            "token" : AuthToken.objects.create(user)[1]
        }, status=status.HTTP_200_OK)
    return Response({
        "error" : "unable to log in"
    }, status = status.HTTP_401_UNAUTHORIZED)

@api_view(['DELETE'])
#deleete2
def user_delete(request,pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    name = user.username
    user.delete()
    return Response({"user deleted" : name}, status=status.HTTP_204_NO_CONTENT)
