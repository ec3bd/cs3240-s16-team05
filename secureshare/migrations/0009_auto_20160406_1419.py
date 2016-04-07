# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secureshare', '0008_auto_20160406_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='short_description',
            field=models.CharField(max_length=200),
        ),
    ]
