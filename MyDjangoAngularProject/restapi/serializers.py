from django.contrib.auth.models import User, Group
from rest_framework import serializers
from restapi.models import Photo, Album


#class PhotoSerializer(serializers.HyperlinkedModelSerializer):
class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'url', 'name', 'album')


#class AlbumSerializer(serializers.HyperlinkedModelSerializer):
class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('name',)