from django.shortcuts import render

# Create your views here.
#from django.contrib.auth.models import User, Group
from restapi.models import Photo, Album
from rest_framework import viewsets
from restapi.serializers import PhotoSerializer, AlbumSerializer


class PhotoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer