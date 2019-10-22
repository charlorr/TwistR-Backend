from django.db import models

class User(models.Model):
    name = models.CharField("Name", max_length=30)
    dob = models.DateField()
    username = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)
    private = models.BooleanField()
    bio = models.CharField(max_length=300)
    joined_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
