from django.db import models
from users.models import User

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text_body = models.CharField(max_length=280)
    like_count = models.IntegerField(default=0)
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author

class Retwist(models.Model):
    original_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='retwist_original_post')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='retwist_post')
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.original_post


class Tag(models.Model):
    name = models.CharField(max_length=20)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
