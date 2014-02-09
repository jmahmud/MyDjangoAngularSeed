from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from restapi import views

admin.autodiscover()
router = routers.DefaultRouter()
router.register(r'photos', views.PhotoViewSet)
router.register(r'albums', views.AlbumViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MyDjangoAngularProject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^(.*)$', include('djangoapp.urls')),
)
