from django.db import models
from django.contrib.auth.models import User

class Journal(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    user = models.ForeignKey(User)