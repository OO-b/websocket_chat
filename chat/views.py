from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def index(request):
    return render(request, 'chat/index.html')

def room(request, room_name):
    id = "111@naver.com"
    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'id': id
    })