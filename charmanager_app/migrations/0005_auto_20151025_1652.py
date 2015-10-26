# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('charmanager_app', '0004_auto_20151025_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercharacter',
            name='username',
            field=models.CharField(unique=True, max_length=30, error_messages={'unique': 'A user with that username already exists.'}, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], verbose_name='username'),
        ),
    ]
