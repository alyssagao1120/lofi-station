from django.shortcuts import render, get_object_or_404
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder

from music_player.models import Song, Artwork
from random import shuffle


# Create your views here.
def play_music(request):
    songs = Song.objects.all()
    songs_list = list(songs)
    shuffle(songs_list)
    songs_list = serializers.serialize("json",songs_list)
    artwork = Artwork().randomArtwork()
    # print(artwork)    
    context = {
        "artwork" : artwork,
        "songs" : songs_list,
    }
    return render(request, 'music_player/play-music.html', context )

def set_artwork_for_music_player(request,id):
    songs = Song.objects.all()
    songs_list = list(songs)
    shuffle(songs_list)
    songs_list = serializers.serialize("json",songs_list) 
    artwork = get_object_or_404(Artwork, pk = id)
    context = {
        "artwork" : artwork,
        "songs" : songs_list,
    }
    return render(request, 'music_player/play-music.html', context)

def full_screen(request, id) :
    songs = Song.objects.all()
    songs_list = list(songs)
    shuffle(songs_list)
    songs_list = serializers.serialize("json",songs_list) 
    artwork = get_object_or_404(Artwork, pk = id)
    context = {
        "artwork" : artwork,
        "songs" : songs_list,
    }
    return render(request, 'music_player/full-screen.html', context )