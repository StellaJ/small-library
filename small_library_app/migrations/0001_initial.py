# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=50, verbose_name=b'Author')),
                ('title', models.CharField(max_length=150, verbose_name=b'Title')),
                ('ISBN', models.CharField(max_length=13, verbose_name=b'ISBN')),
                ('published', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.FileField(upload_to=b'desc/', verbose_name=b'Description')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Reviewer')),
                ('title', models.CharField(max_length=150, verbose_name=b'Title')),
                ('content', models.TextField(verbose_name=b'Comment')),
                ('published', models.DateTimeField(default=django.utils.timezone.now)),
                ('book', models.ForeignKey(to='small_library_app.Book')),
            ],
        ),
    ]
