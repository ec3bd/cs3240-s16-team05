# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secureshare', '0010_auto_20160411_1859'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grouppage',
            name='group',
        ),
        migrations.DeleteModel(
            name='GroupPage',
        ),
    ]
