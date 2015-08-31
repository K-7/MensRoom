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



class UserSession(BaseModel):
    user = models.ForeignKey(UserProfile)
    device_type = models.CharField(max_length=10)
    device_id = models.CharField(max_length=100)
    registration_id = models.CharField(max_length=255, null=True, blank=True)
    session_id = models.CharField(max_length=255)
    user_agent = models.CharField(max_length=1000)
    sync_contacts = models.BooleanField(default=False)
    api_version = models.IntegerField(null=True, blank=True)
    app_version = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = "user_session"