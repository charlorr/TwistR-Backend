from django.db import models

class User(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField("Phone Number", max_length=30, default='')
    first_name = models.CharField("First Name", max_length=30, default='')
    last_name = models.CharField("Last Name", max_length=30, default='')
    password = models.CharField(max_length=30, default='')
    bio = models.CharField(max_length=300, default='')
    joined_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
