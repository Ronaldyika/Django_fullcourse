from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Message

from django.contrib.auth import logout

@login_required
def home(request):
    users = User.objects.exclude(id=request.user.id)
    return render(request, 'home.html', {'users': users})

@login_required
def room(request, recipient_id):
    recipient = get_object_or_404(User, id=recipient_id)
    messages = Message.objects.filter(sender=request.user, recipient=recipient) | Message.objects.filter(sender=recipient, recipient=request.user)
    messages = messages.order_by('timestamp')
    return render(request, 'room.html', {'recipient': recipient, 'messages': messages})

@login_required
def send_message(request, recipient_id):
    if request.method == 'POST':
        recipient = get_object_or_404(User, id=recipient_id)
        content = request.POST.get('content')
        message = Message(sender=request.user, recipient=recipient, content=content)
        message.save()
        return redirect('room', recipient_id=recipient_id)
    else:
        return redirect('home')
    
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        messages.success(request, f'Account created for {username}!')
        return redirect('home')
    else:
        return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')