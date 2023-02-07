from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import AlbomViewSet, ArtistViewSet, SongViewSet

router = DefaultRouter()
router.register('songs', SongViewSet)
router.register('albums', AlbomViewSet)
router.register('artist', ArtistViewSet)


urlpatterns = [
    path('', include(router.urls), name='songs'),
    path('', include(router.urls), name='albums'),
    path('', include(router.urls), name='artists'),
]







