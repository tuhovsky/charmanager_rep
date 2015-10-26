# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('charmanager_app', '0002_auto_20151018_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercharacter',
            name='username',
            field=models.CharField(validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], error_messages={'unique': 'A user with that username already exists.'}, unique=True, verbose_name='username', max_length=30),
        ),
    ]
