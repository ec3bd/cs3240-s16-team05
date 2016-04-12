# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secureshare', '0004_folder_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='folder',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
