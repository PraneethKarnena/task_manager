from django.conf import settings
from django.db import models

from core.models import BaseModel


class Task(BaseModel):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='tasks_created')
    assignee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='tasks_assigned')

    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Project(BaseModel):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    duration_in_months = models.PositiveSmallIntegerField(null=True, blank=True)
    avatar = models.ImageField(null=True, blank=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name