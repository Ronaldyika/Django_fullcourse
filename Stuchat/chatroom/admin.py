from django.contrib import admin

from .models import RegisterStudent,RegisterTeacher,Assigment

# Register your models here.
admin.site.register(RegisterStudent)
admin.site.register(RegisterTeacher)
admin.site.register(Assigment)
