from django.shortcuts import render, redirect
from music_player.models import Artwork
from django.forms import modelform_factory
from .forms import ArtworkForm
# Create your views here.


# ArtworkForm = modelform_factory(UnapprovedArtwork, exclude=[])

def submit_artwork(request) :
    if request.method =="POST":
        form = ArtworkForm(data=request.POST, files=request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('/submit-artwork/thank-you')
    else:
        form = ArtworkForm()
    return render(request, 'submit_artwork/submit-artwork.html', {"form": form})


def thank_you(request):
    return render(request, 'submit_artwork/thank-you.html')