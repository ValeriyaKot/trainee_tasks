from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profiles')
    country = models.CharField(max_length=250, blank=True, null=True)
    b_day = models.DateField()
