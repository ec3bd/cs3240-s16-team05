# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secureshare', '0004_auto_20160404_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='encrypt',
            field=models.BooleanField(default=False),
        ),
    ]
