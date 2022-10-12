from django.contrib import admin
from django.urls import path, include
from chat.views import chat_box

urlpatterns = [
    path("admin/", admin.site.urls),
    path('chat/', include('chat.urls')),
]
