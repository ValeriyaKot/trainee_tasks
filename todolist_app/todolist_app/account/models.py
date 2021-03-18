from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    b_day = models.DateField()
    #
    # def __str__(self):
    #     return self.user.name
