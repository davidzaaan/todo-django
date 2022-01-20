from django.db import models
import uuid
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey, OneToOneField


class UserTaskProfile(models.Model):
    user = OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, unique=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name

class Task(models.Model):
    owner = ForeignKey(UserTaskProfile, blank=True, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=100)
    task_description = models.TextField(max_length=300, null=True, blank=True)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.task_name