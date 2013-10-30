from django.db import models

class Journal(models.Model):
    title = models.CharField()
    text = models.CharField()