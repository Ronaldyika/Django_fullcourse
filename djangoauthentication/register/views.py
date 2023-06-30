from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Users

# Create your views here.
def Homepage(request):
    return render(request,'auth_system/index.html')

def Register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        new_user = Users(firstname = firstname,lastname =lastname,username = username,
                                        email=email,password = password)
        
        new_user.save()
        return redirect('login')
    
    return render(request,'auth_system/register.html')

def Login(request):
    return render(request,'auth_system/login.html')