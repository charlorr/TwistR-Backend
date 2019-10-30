from django.db import models
from django.contrib.auth.models import AbstractUser
# from posts.models import Tag

import datetime

class User(AbstractUser):
    pass    #what the heck is this
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone_number', 'first_name', 'last_name', 'password', 'bio', 'joined_date']

    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField("Phone Number", max_length=30, default='')
    first_name = models.CharField("First Name", max_length=30, default='')
    last_name = models.CharField("Last Name", max_length=30, default='')
    password = models.CharField(max_length=30, default='')
    bio = models.CharField(max_length=300, default='')
    joined_date = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.username

class Twist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='twist_user')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='twist_author')
    # tag = model.ForeignKey(Tag, on_delete=model.CASCADE)

    def __str__(self):
        return self.user

