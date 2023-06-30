from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('room/<int:recipient_id>/', views.room, name='room'),
    path('room/<int:recipient_id>/send_message/', views.send_message, name='send_message'),
    path('', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]