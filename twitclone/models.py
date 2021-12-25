from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import RegexValidator

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None,is_active=True,is_staff=False,is_admin=False):
        """
        Creates and saves a User with the given email and password.
        """
        
        if not username:
            raise ValueError('User must have a username')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, username, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            username,
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            username,
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    username = models.CharField(max_length=36, unique=True, validators=[
        RegexValidator('[a-zA-Z0-9\-_]+', 'Username can only contain letters, numbers, dashes and underscores')
    ])
    email = models.EmailField()
    bio = models.TextField(max_length=280, blank=True, null=True)
    profile_picture = models.ImageField(blank=True, null=True)

    objects = UserManager()


class Tweet(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    quoted_tweet = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL)
    text = models.TextField(max_length=280)
