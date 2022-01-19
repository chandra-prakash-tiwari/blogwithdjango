from asyncio.windows_events import NULL
from django.db import models
from django.contrib.auth.models import User

class Authentication(models.Model):
    username = models.TextField(max_length=50, null=True)
    password = models.CharField(max_length=50)

# class UserProfile(User):
#     firstname = models.CharField(max_length=50)
#     lastname = models.CharField(max_length=50)

#     class Meta:
#         db_table='user_profile'
