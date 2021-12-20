from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class User(AbstractUser):
    username = models.CharField(max_length=36, unique=True, validators=[
        RegexValidator('[a-zA-Z0-9\-_]+', 'Username can only contain letters, numbers, dashes and underscores')
    ])
    email = models.EmailField()
    bio = models.TextField(max_length=280)
    profile_picture = models.ImageField()


class Tweet(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    quoted_tweet = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL)
    text = models.TextField(max_length=280)
