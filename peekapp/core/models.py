__author__ = 'K2A'
from django.db import models


class BaseModel(models.Model):
    '''
        extended by all models
    '''

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    deleted_date = models.DateTimeField(null=True, blank=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True