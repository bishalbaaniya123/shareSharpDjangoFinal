from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.homepage),
    url(r'^upload$', views.upload),
    url(r'^upload_picture$', views.upload_picture),
]
