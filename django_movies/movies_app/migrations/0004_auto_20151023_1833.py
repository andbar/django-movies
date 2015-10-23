# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from data_load import load_ratings


class Migration(migrations.Migration):

    dependencies = [
        ('movies_app', '0003_auto_20151023_1732'),
    ]

    operations = [
        migrations.RunPython(load_ratings)
    ]
