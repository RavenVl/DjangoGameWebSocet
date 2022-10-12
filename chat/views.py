from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def chat_box(request, chat_box_name=None):
    # we will get the chatbox name from the url
    return render(request, "chat/chatbox.html", {"chat_box_name": chat_box_name})
