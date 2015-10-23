# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Rater',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=1)),
                ('occupation', models.CharField(max_length=50)),
                ('zip_code', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('movie', models.ForeignKey(to='movies_app.Movie')),
                ('rater', models.ForeignKey(to='movies_app.Rater')),
            ],
        ),
    ]
