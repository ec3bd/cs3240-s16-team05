# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secureshare', '0011_auto_20160412_1048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='random',
        ),
    ]
