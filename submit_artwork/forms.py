from django import forms
from music_player.models import Artwork
# from music_player import models

class ArtworkForm(forms.ModelForm ):
    class Meta:
        model = Artwork
        fields  = (
            'title',
            'description',
            'artist',
            'file',

        )
    # title = forms.CharField(max_length=500, default="Untitled")
    # description = forms.TextField()
    # artist = forms.CharField(max_length=500, default="Unknown")
    # file = forms.FileField(upload_to="unapproved-artworks/")
    # approved = forms.BooleanField(initial=False)
