# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secureshare', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='tags',
            field=models.CharField(null=True, max_length=300),
        ),
    ]
