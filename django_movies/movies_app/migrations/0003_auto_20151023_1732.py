# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from data_load import load_raters, load_movies, load_ratings


class Migration(migrations.Migration):

    dependencies = [
        ('movies_app', '0002_auto_20151023_1712'),
    ]

    operations = [
        migrations.RunPython(load_raters),
        migrations.RunPython(load_movies)
    ]
