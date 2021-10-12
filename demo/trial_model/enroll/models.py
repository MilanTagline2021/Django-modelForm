from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Student(models.Model):
    stui = models.IntegerField(primary_key=True)
    stuname = models.CharField(max_length=70)
    stuemail = models.EmailField(max_length=70)
    stupass = models.CharField(max_length=70)
    comment = models.CharField(max_length=40, default='N/A')

class Reporter(models.Model):
    """many-to-one relationship"""
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Articles(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=CASCADE)

    def __str__(self):
        return self.headline


class User(models.Model):
    """many-to-many relationship"""
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.user_name

class Song(models.Model):
    user = models.ManyToManyField(User)
    song_name = models.CharField(max_length=50)
    song_duration = models.IntegerField()

    def __str__(self):
        return f'{self.song_name} {self.user}'

    
class Register(models.Model):
    """one-to-one relationship"""
    user_name = models.CharField(max_length=50)
    password = models.IntegerField()

    def __str__(self):
        return self.user_name

class Course(models.Model):
    register = models.OneToOneField(Register,on_delete=CASCADE)
    course_name = models.CharField(max_length=70)

    def __str__(self):
        return f'{self.course_name} {self.register}'


class Teacher(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=16)

    class Meta:
        abstract = True

class Manage(Teacher):
    confirm_password = models.CharField(max_length=16)


class RestInform(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=16)
    confirm_password = models.CharField(max_length=16)