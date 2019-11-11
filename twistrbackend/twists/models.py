from django.db import models
from users.models import User
from posts.models import Tag

# Create your models here.
class Twist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='twist_user')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='twist_author')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return self.user

