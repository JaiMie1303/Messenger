from django.contrib import admin

from .models import ChatUser, Message, ChatRoom

admin.site.register(ChatUser)
admin.site.register(Message)
admin.site.register(ChatRoom)
