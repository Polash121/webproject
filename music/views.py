from django.shortcuts import render
from .models import Album

# Create your views here.


def home(request):
    return render(request, 'music/home.html', None)


def albums(request):
    albums = Album.objects.all()
    return render(request, 'music/Albums.html', albums)
