from .models import StudentInfo
from django import forms

class studentform(forms.ModelForm):
    class Meta:
        model = StudentInfo
        fields = '__all__'
