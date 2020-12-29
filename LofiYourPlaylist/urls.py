"""LofiYourPlaylist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from home.views import home
from music_player.views import play_music, set_artwork_for_music_player, full_screen
from all_songs.views import all_songs
from all_artworks.views import all_artworks 
from submit_artwork.views import submit_artwork, thank_you


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('home/', home, name="home"),
    path('play-music/', play_music, name="play_music"),
    path('play-music/<int:id>', set_artwork_for_music_player, name="set_artwork_for_music_player"),
    path('play-music/full-screen/<int:id>', full_screen, name="full_screen"),
    path('all-songs/', all_songs, name="all_songs"),
    path('all-artworks/', all_artworks, name="all_artworks"),
    path('submit-artwork/', submit_artwork, name="submit_artwork"),
    path('submit-artwork/thank-you/', thank_you, name="thank_you"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# handler404 = 'home.views.error_404_view'
