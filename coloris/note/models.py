from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=240)
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
