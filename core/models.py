from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True
        ordering = ['-created_at']


class User(AbstractUser, BaseModel):
    email = models.EmailField(unique=True)

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    class Meta:
        ordering = ['first_name', 'last_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.email}'