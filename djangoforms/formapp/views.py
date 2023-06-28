from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import studentform
from .models import StudentInfo


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = studentform(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = studentform()
        return render(request,'index.html',{'form':form})
