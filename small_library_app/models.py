#-*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

class Book(models.Model):
	author = models.CharField(max_length=50, verbose_name="Author")
	title = models.CharField(max_length=150, verbose_name="Title")
	ISBN = models.CharField(max_length=13, verbose_name="ISBN")
	published = models.DateTimeField(default=timezone.now)
	link = models.CharField(max_length=400, verbose_name="Link")

	def __unicode__(self):
		return self.title + " " + self.author

class Review(models.Model):
	name = models.CharField(max_length=50, verbose_name="Reviewer")
	title = models.CharField(max_length=150, verbose_name="Title")
	content = models.TextField(verbose_name="Comment")
	published = models.DateTimeField(default=timezone.now)
	book = models.ForeignKey(Book)

	def __unicode__(self):
		return self.name + " " + self.title