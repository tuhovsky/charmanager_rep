# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charmanager_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='title',
            field=models.CharField(error_messages={'unique': 'That skill already exists.'}, max_length=255, unique=True),
        ),
    ]
