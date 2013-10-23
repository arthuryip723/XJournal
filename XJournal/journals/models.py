from django.db import models

class Journal(models.Model):
    text = models.CharField()