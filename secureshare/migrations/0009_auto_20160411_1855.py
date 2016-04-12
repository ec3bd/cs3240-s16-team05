# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secureshare', '0008_auto_20160411_1851'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='folder',
            name='reports',
        ),
        migrations.AddField(
            model_name='folder',
            name='reports',
            field=models.ManyToManyField(to='secureshare.Report'),
        ),
    ]
