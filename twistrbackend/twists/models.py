from django.db import models
from users.models import User
from posts.models import Post, Tag

class Twist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='twist_user')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='twist_author')
    tag = models.CharField(max_length=20)

    def __str__(self):
        return self.user

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like_user')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='like_post')

    def __str__(self):
        return self.user
