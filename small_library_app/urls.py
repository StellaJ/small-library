#-*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf import settings
from . import views

urlpatterns = patterns('',
    (r'^home/$', 'library.views.home'),
    (r'^new_book/$', 'library.views.new_book'),
    (r'^show_book/(?P<book_id>\d+)/$', 'library.views.show_book'),
    (r'^(?P<id>\d+)/delete_book/$', 'library.views.delete_book'),
    (r'^reviews/$', 'library.views.reviews'),

    (r'^(?P<book_id>\d+)/new_review/$', 'library.views.new_review'),
    (r'^show_review/(?P<review_id>\d+)/$', 'library.views.show_review'),
    (r'^edit_review/(?P<review_id>\d+)/$', 'library.views.edit_review'),
    (r'^(?P<id>\d+)/delete_review/$', 'library.views.delete_review'),

)