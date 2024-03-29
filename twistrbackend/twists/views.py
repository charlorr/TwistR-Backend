from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status

from rest_framework.permissions import AllowAny

from .models import Twist, Like
from .serializers import *

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
        tag_param = request.query_params.get('tag', None)

        if user_param is not None:
            data = data.filter(user=user_param)

        if author_param is not None:
            data = data.filter(author=author_param)

        if tag_param is not None:
            data = data.filter(tag=tag_param)

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

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((AllowAny,))
def twists_by_author(request, pku, pka):
    """
 Retrieve, update or delete a twist by id/pk of the author.
 """
    try:
        twist = Twist.objects.get(user=pku, author=pka)
    except Twist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = TwistSerializer(twist,context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes((AllowAny,))
def twists_by_user(request, pk):
    """
 Get all twists by id/pk of the user.
 """
    try:
        twist = Twist.objects.get(user=pk)
    except Twist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = TwistSerializer(twist,context={'request': request})
    return Response(serializer.data)

# Like stuff

@api_view(['GET', 'POST', 'DELETE'])
@permission_classes((AllowAny,))
def likes_list(request):
    """
 List likes, or create a new like.
 """
    if request.method == 'GET':
        data = []

        data = Like.objects.all()
        user_param = request.query_params.get('user', None)
        post_param = request.query_params.get('post', None)

        if user_param is not None:
            data = data.filter(user=user_param)

        if post_param is not None:
            data = data.filter(post=post_param)

        serializer = LikeSerializer(data,context={'request': request},many=True)

        return Response({'data': serializer.data})

    elif request.method == 'POST':
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        data = Like.objects.all()
        user_param = request.query_params.get('user', None)
        post_param = request.query_params.get('post', None)

        if user_param is not None:
            data = data.filter(user=user_param)

        if post_param is not None:
            data = data.filter(post=post_param)


        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'DELETE'])
@permission_classes((AllowAny,))
def likes_detail(request, pku, pkp):
    """
 Retrieve, update or delete a like by id/pk of the user and post.
 """
    try:
        like = Like.objects.get(user=pku, post=pkp)
    except Like.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LikeSerializer(twist,context={'request': request})
        return Response(serializer.data)

    elif request.method == 'DELETE':
        like.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
