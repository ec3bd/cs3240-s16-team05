# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('secureshare', '0019_auto_20160409_0006'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='auth_users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
