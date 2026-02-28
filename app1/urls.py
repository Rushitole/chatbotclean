from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_page, name="chat"),
    path('stream/', views.chat_stream, name="chat_stream"),
]