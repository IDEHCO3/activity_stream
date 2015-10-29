from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Follower(models.Model):
    user = models.ForeignKey(User, related_name='follows')
    following = models.ForeignKey(User)
    since = models.DateTimeField(auto_now_add=True)