#-*- coding: utf-8 -*-
from django import forms
from models import *

class BookForm(forms.Form):

	author = forms.CharField(label="Author", max_length=50)
	title = forms.CharField(label="Title", max_length=200)
	ISBN = forms.CharField(label="ISBN", max_length=13)
	published = forms.DateTimeField(label="Date of publication")
	description = forms.FileField(label="Description", help_text='max. 10 MB')

class ReviewForm(forms.ModelForm):

	class Meta:
		model = Review
		fields = ('name', 'title', 'content')