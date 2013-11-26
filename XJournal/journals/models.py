from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

class Journal(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    private = models.BooleanField()
    user = models.ForeignKey(User)
    
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.title
    # Add a boolean field here to indicate whether it is public or private
    
class JournalForm(ModelForm):
    class Meta:
        model = Journal
        exclude = ['user']