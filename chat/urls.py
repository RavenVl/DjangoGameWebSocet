from django.urls import path

from . import views

urlpatterns = [
    path('', views.chat_box, name='index'),
    path("<str:chat_box_name>/", views.chat_box, name="chat"),
]
