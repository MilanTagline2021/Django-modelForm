from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=240)
    desc = models.TextField()