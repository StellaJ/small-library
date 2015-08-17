#-*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf import settings
from . import views

urlpatterns = patterns('',
    (r'^home/$', 'small_library_app.views.home'),
    (r'^new_book/$', 'small_library_app.views.new_book'),
    (r'^show_book/(?P<book_id>\d+)/$', 'small_library_app.views.show_book'),
    (r'^(?P<id>\d+)/delete_book/$', 'small_library_app.views.delete_book'),
    (r'^reviews/$', 'small_library_app.views.reviews'),
    (r'^show_book/(?P<book_id>\d+)/boook.url.link/$', 'small_library_app.views.show_book'),


    (r'^(?P<book_id>\d+)/new_review/$', 'small_library_app.views.new_review'),
    (r'^show_review/(?P<review_id>\d+)/$', 'small_library_app.views.show_review'),
    (r'^edit_review/(?P<review_id>\d+)/$', 'small_library_app.views.edit_review'),
    (r'^(?P<id>\d+)/delete_review/$', 'small_library_app.views.delete_review'),

)