from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

class Journal(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    user = models.ForeignKey(User)
    private = models.BooleanField()
    # Add a boolean field here to indicate whether it is public or private
    
class JournalForm(ModelForm):
    class Meta:
        model = Journal