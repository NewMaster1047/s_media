from django.db import models
from django.contrib.auth.models import User


class MyUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.username
