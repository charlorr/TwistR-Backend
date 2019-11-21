from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status

from rest_framework.permissions import AllowAny

from .models import Post, Tag
from users.models import User
from twists.models import Twist
from .serializers import *
from users.serializers import *

# Gets posts by a user in reverse order (most recent first)

@api_view(['GET'])
@permission_classes((AllowAny,))
def posts_by_user(request, pk):
    """
 List posts written by a specified user.
 """
    data = []

    data = Post.objects.filter(author=pk).order_by('-posted_date')

    serializer = PostSerializer(data,context={'request': request},many=True)

    return Response({'data': serializer.data})

@api_view(['GET'])
@permission_classes((AllowAny,))
def tags_by_user(request, pk):
    """
 Get all of user's tags.
 """
    tags = []

    tag_names = Tag.objects.filter(post__author=pk).values_list('name', flat=True).distinct()

    for tag_name in tag_names:
        tags.append(Tag.objects.filter(name=tag_name).first())

    serializer = TagSerializer(tags,context={'request': request},many=True)

    return Response({'data': serializer.data})

@api_view(['GET'])
@permission_classes((AllowAny,))
def tags_by_post(request, pk):
    """
 Get a post's tags.
 """
    data = []

    data = Tag.objects.filter(post=pk)

    serializer = TagSerializer(data,context={'request': request},many=True)

    return Response({'data': serializer.data})

# Lists all posts sorted by most recent-- Can be used for explore page

@api_view(['GET', 'POST'])
@permission_classes((AllowAny,))
def posts_list(request):
    """
 List posts, or create a new post.
 """
    if request.method == 'GET':
        data = []

        data = Post.objects.all().order_by('-posted_date')

        serializer = PostSerializer(data,context={'request': request},many=True)

        return Response({'data': serializer.data})

    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
@permission_classes((AllowAny,))
def tags_list(request):
    """
 List posts, or create a new post.
 """
    if request.method == 'GET':
        data = []

        data = Tag.objects.all()

        serializer = TagSerializer(data,context={'request': request},many=True)

        return Response({'data': serializer.data})

    elif request.method == 'POST':
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((AllowAny,))
def posts_detail(request, pk):
    """
 Retrieve, update or delete a post by id/pk.
 """
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostSerializer(post,context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((AllowAny,))
def tags_detail(request, pk):
    """
 Retrieve, update or delete a tag by id/pk.
 """
    try:
        tag = Tag.objects.get(pk=pk)
    except Tag.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TagSerializer(tag,context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TagSerializer(tag, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        tag.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Get all posts for timeline based on twists

@api_view(['GET'])
@permission_classes((AllowAny,))
def relevant_posts(request, pk):
    """
 Get posts in accordance with a user's twists
 """

    # Get objects posts from a user first

    twists = Twist.objects.filter(user=pk)

    author_pks = twists.values_list('author', flat=True)
    tag_names = twists.values_list('tag', flat=True)

    data = []
    data = Post.objects.filter(author__in=author_pks).order_by('-posted_date').filter(tag__name__in=tag_names).distinct()

    serializer = PostSerializer(data,context={'request': request},many=True)

    return Response({'data': serializer.data})
