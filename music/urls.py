"""firstapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name="index"),
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name="detail"),

    url(r'^album/add/$',views.AlbumCreate.as_view(), name="album-add"),
    url(r'^album/(?P<pk>[0-9]+)/$',views.AlbumUpdate.as_view(), name="album-update"),
    url(r'^album/(?P<pk>[0-9]+)/delete/$',views.AlbumDelete.as_view(), name="album-delete"),

    url(r'^song/add/$',views.SongCreate.as_view(), name="song-add"),
	# url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name="favorite"),
]
