from django.contrib.auth.forms import UserCreationForm
from .models import RegisterTeacher,RegisterStudent,Assigment

class studentregistrationform(UserCreationForm):
    class Meta:
        model = RegisterStudent
        #fields = ['studentname','matricule','studentpassword','studentimage']
        fields = '__all__'

class teacherregistrationform(UserCreationForm):
    class Meta:
        model = RegisterTeacher
        fields = '__all__'