from rest_framework import serializers
from .models import Post, Tag

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('pk', 'author', 'text_body', 'posted_date')

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('pk', 'name', 'post')
