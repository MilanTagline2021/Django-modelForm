from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=240)
    desc = models.TextField()

class ContactUs(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=256)
    address = models.CharField(max_length=256)
    message = models.TextField()