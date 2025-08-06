from django.urls import path
from .views import chat_with_bot, chat_ui  # ← Add chat_ui here

urlpatterns = [
    path("", chat_ui, name="chat_ui"),
    path("api/chat/", chat_with_bot, name="chat_with_bot"),
]
