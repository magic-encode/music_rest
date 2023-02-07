from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from music.models.album import Album
from music.models.artist import Artist

from music.models.song import Song


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'
        


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'  
    

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('id', 'title', 'album', 'cover', 'source', 'listened')

    def validate_source(self, value):
        if not value.endswith('.mp3'):
            raise ValidationError(detail='Mp3 file is required...')
        return value

