from django.db import models
from django.contrib.auth.models import User
from .behavior import Timestampable


class ToDoList(Timestampable):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100, db_index=True)
    description = models.TextField(blank=True, null=True)
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_at', 'available']

    def __str__(self):
        return self.title