from rest_framework import serializers
from .models import Post, Retwist, Tag

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('pk', 'author', 'text_body', 'like_count', 'posted_date')

class RetwistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Retwist
        fields = ('pk', 'original_post', 'post', 'author', 'text_body', 'like_count', 'posted_date')

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('pk', 'name', 'post')
