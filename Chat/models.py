from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    room_name = models.CharField(max_length=100, default="")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author.username}'

    def get_last_10_message(self):
        return Message.objects.order_by('-timestamp').all()[:30]
