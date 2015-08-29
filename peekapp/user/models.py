from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

from core.models import BaseModel


class UserProfile(AbstractUser):
    avatar = models.CharField(max_length=500, default="")
    objects = UserManager()

    USERNAME_FIELD = 'username'

    class Meta:
        db_table = "userprofile"

    def get_full_name(self):
        # The user is identified by their email address
        return self.username

    def __str__(self):              # __unicode__ on Python 2
        return self.email


