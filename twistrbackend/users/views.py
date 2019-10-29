from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import User
from .serializers import *

@api_view(['GET', 'POST'])
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

        serializer = UserSerializer(data,context={'request': request},many=True)

        return Response({'data': serializer.data  })

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def users_detail(request, pk):
    """
 Retrieve, update or delete a user by id/pk.
 """
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user,context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
