from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.


def index(request):
    anime = Anime.objects.all()
    popular = Popular.objects.all()
    action = Action.objects.all()
    kids = Kids.objects.all()
    family = Family.objects.all()
    context = {'anime': anime, 'popular': popular, 'action': action, 'kids': kids, 'family': family}
    return render(request, 'core/index.html', context)

def anime_video(request, anime_id):
    anime = get_object_or_404(Anime, id=anime_id)
    videos = Video.objects.filter(anime=anime)
    return render(request, 'core/watch.html', {'anime': anime, 'videos': videos})
