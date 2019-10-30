from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status, permissions
from knox.models import AuthToken

from .models import User, Twist
from .serializers import *

# Add decorator if the endpoint does not require authentication, or for testing
# @permission_classes((AllowAny,))

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

        serializer = TwistSerializer(data,context={'request': request},many=True)

        return Response({'data': serializer.data})

    elif request.method == 'POST':
        serializer = TwistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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



# @api_view(['GET'])
# @permission_classes((AllowAny,))
# def followers_by_user(request, pk):
#     """
#  Get users following specified user
#  """
#     try:
#         user = User.objects.get(pk=pk)
#     except User.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     data = Twists.objects.filter(author=pk)

#     serializer = TwistSerializer(twist,context={'request': request})
#     return Response(serializer.data)


# @api_view(['GET'])
# @permission_classes((AllowAny,))
# def following_by_user(request, pk):
#     """
#  Get users a specified user follows
#  """
#     try:
#         user = User.objects.get(pk=pk)
#     except User.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     data = Twist.objects.filter(user=pk)

#     serializer = TwistSerializer(twist,context={'request': request})
#     return Response(serializer.data)
