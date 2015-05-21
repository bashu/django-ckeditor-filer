# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ThumbnailOption',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('width', models.IntegerField(help_text='width in pixel.', verbose_name='width')),
                ('height', models.IntegerField(help_text='height in pixel.', verbose_name='height')),
                ('crop', models.BooleanField(default=True, verbose_name='crop')),
                ('upscale', models.BooleanField(default=True, verbose_name='upscale')),
            ],
            options={
                'ordering': ('width', 'height'),
                'verbose_name': 'thumbnail option',
                'verbose_name_plural': 'thumbnail options',
            },
        ),
    ]
