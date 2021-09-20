from django.contrib import admin
from Chat.models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    fields = ['room_name', 'author', 'content', 'timestamp']
    list_display = ['room_name', 'author', 'content', 'timestamp']
