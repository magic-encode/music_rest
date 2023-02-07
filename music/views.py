from django.db import transaction
from rest_framework import status

from music.models.song import Song
from music.models.album import Album
from music.models.artist import Artist

from music.serializers import SongSerializer
from music.serializers import AlbumSerializer
from music.serializers import ArtistSerializer

from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination


class SongViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    pagination_class = LimitOffsetPagination
    
    @action(detail=True, methods=['POST'])
    def listen(self, request, *args, **kwargs):
        with transaction.atomic():
            song = self.get_object()
            song.listened +=1
            song.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    @action(detail=False, methods=['GET'])
    def top(self, request, *args, **kwargs):
        songs = self.get_queryset()
        songs = songs.order_by('-listened')[:10]
        serializer = SongSerializer(songs, many=True)
        return Response(data=serializer.data)


class AlbomViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    @action(detail=True, methods=['GET'])
    def albums(self, request, *args, **kwargs):
        artist = self.get_object()
        serializer = AlbumSerializer(artist.album_set.all(), many=True)

        return Response(serializer.serialize.data)
    