from django.db import models

# Create your models here.
class Message(models.Model):
    chat_room = models.CharField(max_length=256)
    content = models.TextField()
    send_time = models.DateTimeField(auto_now_add=True)
