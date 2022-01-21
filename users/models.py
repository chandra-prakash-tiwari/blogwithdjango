from asyncio.windows_events import NULL
from django.db import models
from django.contrib.auth.models import User

class Authentication(models.Model):
    username = models.TextField(max_length=50, null=True)
    password = models.CharField(max_length=50)

# class UserProfile(models.Model):
#     user   = models.OneToOneField(User, on_delete=models.CASCADE)
#     avatar = models.ImageField(upload_to='avatar/%Y/%m', default='avatar/default.png', max_length=200)
#     phone  = models.CharField(max_length=20, null=True)

#     def __str__(self):
#         return 'user {}'.format(self.user.username)


class Users(User):
    avatar = models.ImageField(upload_to='avatar/%Y', max_length=200, null=True)
    phone = models.CharField(max_length=12, null=True)

    def __str__(self):
        return 'user {}'.format(self.username)

        
        




