from django.urls import path
from django.conf import settings
from .views import MusicViewSet

urlpatterns = [
    path("v1/music", MusicViewSet.as_view({"get": "list", "post": "add"}), name="music"),
    path("v1/music/<int:music_num>", MusicViewSet.as_view({"get": "list"}), name="music"),
    path("v1/music/map", MusicViewSet.as_view({"get": "view_map"}), name="music"),
]