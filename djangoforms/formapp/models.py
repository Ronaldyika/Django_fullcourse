from django.db import models

# Create your models here.
class StudentInfo(models.Model):
    name = models.CharField(max_length=255, null=True)
    date_of_birth = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
