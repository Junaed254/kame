from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('anime/<int:anime_id>/video/', views.anime_video, name='anime_video'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
