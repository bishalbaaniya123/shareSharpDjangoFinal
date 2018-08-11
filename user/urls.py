from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.homepage),
    url(r'^upload$', views.upload),
    url(r'^getListOfImageUrls$', views.getListOfImageUrls),
    url(r'^upload_picture$', views.upload_picture),
    url(r'^getListOfLans$', views.getListOfLans),
    url(r'^sendPic/(?P<lan>[0-9A-Za-z_\-]+)/(?P<user_name>[0-9A-Za-z_\-]+)', views.sendPic),
    url(r'^receive$', views.receive),
    url(r'^receivePhotos$', views.receive_photos),
    url(r'^sendButtonPressed/(?P<userName>[0-9A-Za-z_\-]+)/$', views.sendButtonPressed),
    url(r'^user_details/(?P<user_name>[0-9A-Za-z_\-]+)/$', views.user_details),
]
