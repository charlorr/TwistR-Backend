from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status, permissions
#from rest_framework.authtoken.models import Token
from knox.models import AuthToken
from django.core.mail import send_mail
from .models import User

from .models import User, Twist
from .serializers import *
from django.conf import settings

#use this if the endpoint does not require authentication
#@permission_classes((AllowAny,))

@api_view(['GET'])
@permission_classes((AllowAny,))
def users_list(request):
    """
 List users, or create a new user.
 """
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

@api_view(['GET', 'POST'])
@permission_classes((AllowAny,))
def twists_list(request):
    """
 List twists, or create a new twist.
 """
    if request.method == 'GET':
        data = []

        data = Twist.objects.all()
        user_param = request.query_params.get('user', None)
        author_param = request.query_params.get('author', None)

        if user_param is not None:
            data = data.filter(user=user_param)

        if author_param is not None:
            data = data.filter(author=author_param)

        serializer = TwistSerializer(data,context={'request': request},many=True)

        return Response({'data': serializer.data})

    elif request.method == 'POST':
        serializer = TwistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes((AllowAny,))
def unfollow(request):
    """
 Unfollow a user by deleting the twist that connects the user / author
 """

    data = Twist.objects.all()

    user_param = request.query_params.get('user', None)
    author_param = request.query_params.get('author', None)

    if user_param is not None:
        data = data.filter(user=user_param)

    if author_param is not None:
        data = data.filter(author=author_param)
        data.delete()

    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((AllowAny,))
def twists_detail(request, pk):
    """
 Retrieve, update or delete a twist by id/pk.
 """
    try:
        twist = Twist.objects.get(pk=pk)
    except Twist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TwistSerializer(twist,context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TwistSerializer(twist, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        twist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET'])
@permission_classes((AllowAny,))
def password_by_user(request):
    """
 Get the password by a user's pk.
 """
    #data = []

    #data = PlainPassword.objects.filter(user=pk)

    #serializer = PlainPasswordSerializer(data,context={'request': request},many=True)

    subject = 'You have forgotten your password.'
    message = 'Your password is: asdASD2@'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['aesonakhras@gmail.com',"charlorrnot@gmail.com"]
    send_mail( subject, message, email_from, recipient_list )

    return Response(status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
@permission_classes((AllowAny,))
def password_list(request):
    """
 List posts, or create a new post.
 """
    if request.method == 'GET':
        data = []

        data = PlainPassword.objects.all()

        serializer = PlainPasswordSerializer(data,context={'request': request},many=True)

        return Response({'data': serializer.data})

    elif request.method == 'POST':
        serializer = PlainPasswordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
