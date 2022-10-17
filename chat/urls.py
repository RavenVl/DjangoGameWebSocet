from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chat/', views.chat_box, name='chat-box-index'),
    path("login/", views.login_request, name="login"),
    path("register/", views.register_request, name="register"),
    path("<str:chat_box_name>/", views.chat_box, name="chat-box"),
]
