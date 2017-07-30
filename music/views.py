# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
# from django.http import HttpResponse, Http404
from models import Album, Song
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm

class IndexView(generic.ListView):
	template_name = 'music/index.html'
	context_object_name = 'all_albums'

	def get_queryset(self):
		return Album.objects.all()

class DetailView(generic.DetailView):
	model = Album
	template_name = 'music/detail.html'

class AlbumCreate(CreateView):
	model = Album
	fields = ['artist','album_name', 'genre', 'album_logo']

class AlbumUpdate(UpdateView):
	model = Album
	fields = ['artist','album_name', 'genre', 'album_logo']

class AlbumDelete(DeleteView):
	model = Album
	success_url = reverse_lazy('music:index')

class SongCreate(CreateView):
	model = Song
	template_name = 'music/album_form.html'
	fields = ['album', 'file_type', 'title']

class UserFormView(generic.View):
	form_class = UserForm
	template_name = 'music/registration_form.html'

	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		form = self.form_class(request.POST)
		if form.is_valid():
			user = form.save(commit=False)

			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			user.set_password(password)
			user.save()

			user = authenticate(username=username,password=password)

			if user is  not None:
				if user.is_active:
					login(request,user)
					return redirect('music:index')

		return render(request, self.template_name, {'form': form})

















 
# # Initial Clumsy views
# 
# def index(request):
# 	all_album = Album.objects.all()
# 	context = {
# 		'all_album': all_album,
# 	}
# 	return render(request, 'music/index.html', context)
# 
# def detail(request, album_id):
# 	album = get_object_or_404(Album,pk=album_id)
# 	# songs = Song.objects.filter(album=album_id)
# 	songs = album.song_set.all()
# 	return render(request, 'music/detail.html', {'album':album, 'songs':songs})
# 
# def favorite(request, album_id):
# 	album = get_object_or_404(Album,pk=album_id)
# 	songs = album.song_set.all()
# 	errors = ""
# 	try:
# 		selected_song = album.song_set.get(pk=request.POST['song'])
# 	except (KeyError, Song.DoesNotExist):
# 		errors = "Song not found"		
# 	else:
# 		selected_song.is_fav = not selected_song.is_fav
# 		selected_song.save()
# 	return render(request, 'music/detail.html', {
# 			'album':album,
# 			'errors': errors,
# 			'songs' : songs,
# 			})
