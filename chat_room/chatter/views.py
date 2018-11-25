from django.shortcuts import render
from django.utils.safestring import mark_safe
from chatter import models
import json

# Create your views here.
def index(request):
    return render(request, 'chat/index.html', {})

def room(request, room_name):
    history_chat = []
    for msg in models.Message.objects.filter(chat_room=room_name):
        history_chat.append(msg.content)
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'history_chat': mark_safe(history_chat)
    })