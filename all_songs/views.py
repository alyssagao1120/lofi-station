from django.shortcuts import render
from django.db.models.functions import Lower
from music_player.models import Song

# Create your views here.
def all_songs(request):
    songs = Song.objects.all().order_by(Lower('song_title'))
    songs_list = list(songs)
    context = {
        "songs" : songs_list,
    }
    return render(request, 'all_songs/all_songs.html', context)