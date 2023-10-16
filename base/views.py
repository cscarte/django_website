from django.http import HttpResponse
from django.shortcuts import render
from .models import Room

# Create your views here.

rooms = [
    {'id': 1, 'name': 'Lets learn Python!'},
    {'id': 2, 'name': 'Design with me'},
    {'id': 3, 'name': 'Frontend developers'},
]


def home(request):
    list_rooms = Room.objects.all()
    context = {'rooms': list_rooms}
    return render(request, 'base/home.html', context)


def about(request):
    return HttpResponse("About Page!")


def room(request, pk):
    var_room = None
    for i in rooms:
        if i['id'] == int(pk):
            var_room = i
    context = {'room': var_room}
    return render(request, 'base/room.html', context)
