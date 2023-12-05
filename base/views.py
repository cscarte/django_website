from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm


# Create your views here.

# rooms = [
#     {'id': 1, 'name': 'Lets learn Python!'},
#     {'id': 2, 'name': 'Design with me'},
#     {'id': 3, 'name': 'Frontend developers'},
# ]


def home(request):
    list_rooms = Room.objects.all()
    context = {'rooms': list_rooms}
    return render(request, 'base/home.html', context)


def about(request):
    return HttpResponse("About Page!")


def room(request, pk):
    var_room = Room.objects.get(id=pk)
    context = {'room': var_room}
    # for i in rooms:
    #     if i['id'] == int(pk):
    #         var_room = i
    # context = {'room': var_room}
    return render(request, 'base/room.html', context)


def create_room(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            print(request.POST)
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/room_form.html', context)


def update_room(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)


def delete_room(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'object': room})
