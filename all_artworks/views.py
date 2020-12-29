from django.shortcuts import render
from music_player.models import Artwork

# Create your views here.
def all_artworks (request):
    artworks = Artwork.objects.all().filter(approved=True).order_by('-id')
    # artworks_list = list(artworks)
    context = {
        "artworks" : artworks,
    }
    return render(request, 'all_artworks/all-artworks.html', context)

