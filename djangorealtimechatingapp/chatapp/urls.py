from django.urls import path
from . import views


urlpatterns = [
    path('<str:room_name>/', views.chat_room, name='chat_room'),
    path('<str:room_name>/send_message/', views.send_message, name='send_message'),
]