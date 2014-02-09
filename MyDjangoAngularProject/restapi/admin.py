from django.contrib import admin

# Register your models here.
from restapi.models import Photo, Album
admin.site.register(Photo)
admin.site.register(Album)