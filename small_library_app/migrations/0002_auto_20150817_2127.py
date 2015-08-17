# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('small_library_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='description',
        ),
        migrations.AddField(
            model_name='book',
            name='link',
            field=models.CharField(default=' ', max_length=400, verbose_name=b'Link'),
            preserve_default=False,
        ),
    ]
