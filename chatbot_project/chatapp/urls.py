from django.urls import path
from . import views

urlpatterns = [
    path('', views.chatbot_view, name='chatbot'),
    path('ask/', views.ask_bot, name='ask_bot'),  # AJAX request ke liye
]
