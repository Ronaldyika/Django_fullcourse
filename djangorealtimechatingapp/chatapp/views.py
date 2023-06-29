from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Room, Message


def chat_room(request, room_name):
    room = Room.objects.get(name=room_name)
    messages = Message.objects.filter(room=room)

    return render(request, 'chat/room.html', {'room': room, 'messages': messages})


def send_message(request, room_name):
    room = Room.objects.get(name=room_name)
    text = request.POST.get('message', '')
    message = Message(room=room, text=text, user=request.user, timestamp=timezone.now())
    message.save()
    return redirect('chat_room', room_name=room_name)


def chat_room(request, room_name):
    room = get_object_or_404(Room, name=room_name)
    messages = Message.objects.filter(room=room)
    return render(request, 'chat/room.html', {'room': room, 'messages': messages})