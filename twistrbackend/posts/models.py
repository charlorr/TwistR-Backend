from django.db import models
from users.models import User

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=280)
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author
