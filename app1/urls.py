from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home, name="home"),
    path('', views.chat_page, name="chat"),
    path('stream/', views.chat_stream, name="chat_stream"),
]