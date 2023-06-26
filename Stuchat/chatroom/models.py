from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
#for the teacher site
class RegisterTeacher(models.Model):
    teacherimage = models.ImageField(upload_to='images/')
    teachername = models.CharField(max_length=255,unique=True)
    teacheremail = models.EmailField(max_length=255,unique=True)
    teacherpassword = models.CharField(max_length=40)

    USERNAME_FIELD = 'teachername'


    def __str__(self):
        return self.teachername
    
#this site is to register the students


class RegisterStudent(models.Model):
    studentimage = models.ImageField(upload_to='images/')
    studentname = models.CharField(max_length=255)
    username = models.CharField(max_length=40,null=True)
    matricule = models.CharField(max_length=30,unique=True)
    studentpassword = models.CharField(max_length=40)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.matricule
    
class Assigment(models.Model):
    ass = models.FileField()
