# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Album(models.Model):
	artist = models.CharField(max_length=20)
	album_name = models.CharField(max_length=20)
	genre = models.CharField(max_length=20)
	album_logo = models.CharField(max_length=1000)

	def __str__(self):
		return self.album_name + " - " + self.artist

	def get_absolute_url(self):
		return reverse('music:detail', kwargs={'pk':self.pk})

class Song(models.Model):
	album = models.ForeignKey(Album,on_delete=models.CASCADE)
	file_type = models.CharField(max_length=5)
	title = models.CharField(max_length=20)
	is_fav = models.BooleanField(default=False)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('music:detail', kwargs={'pk':self.album.pk})