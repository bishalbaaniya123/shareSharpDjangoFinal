from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.homepage),
    url(r'^upload$', views.upload),
    url(r'^upload2$', views.upload2),
]