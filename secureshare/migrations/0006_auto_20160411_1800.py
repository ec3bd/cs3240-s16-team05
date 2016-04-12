# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secureshare', '0005_folder_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='reports',
            field=models.ForeignKey(null=True, to='secureshare.Report'),
        ),
    ]
