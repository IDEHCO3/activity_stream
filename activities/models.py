from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Activity(models.Model):
    author = models.ForeignKey(User)
    action = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    creation_date = models.DateTimeField(auto_now_add=True)