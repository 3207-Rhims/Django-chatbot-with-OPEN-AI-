from django.urls import path
from . import views

urlpatterns = [
    path('chatbot/', views.chatbot, name='chatbot'),
    path('chatbot/get_response/', views.get_response, name='get_response'),
]