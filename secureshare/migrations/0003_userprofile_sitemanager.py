# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secureshare', '0002_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='siteManager',
            field=models.BooleanField(default=False),
        ),
    ]
