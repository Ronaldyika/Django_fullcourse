from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import SignUp
from django.contrib.auth.models import User,auth

# Create your views here.
def signup(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']

        if (password == password1):
            if SignUp.objects.filter(username = username).exists():
                messages.info(request,'username already taken')
                return render(request,'signup.html')
            else:
                user = SignUp.objects.create_user(username=username,password=password)
                user.save()
                return redirect('signin')
        else:
            messages.info(request,'password doesnot match')
            return render(request,'signup.html')
    else:
            
        return render(request,'signup.html')


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username,password = password)

        if user is not None:

            auth.login(request,user)
            return redirect("/")
        
        else:
            messages.info(request,'invalid credentials')
            return redirect('signin')
        
    
    return render(request,'signin.html')

def index(request):
    return render(request,'index.html')