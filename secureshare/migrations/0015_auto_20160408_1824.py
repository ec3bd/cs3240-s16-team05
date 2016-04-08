# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secureshare', '0014_auto_20160408_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='file2',
            field=models.FileField(default=None, upload_to='files//%Y%m%d'),
        ),
        migrations.AlterField(
            model_name='report',
            name='file3',
            field=models.FileField(default=None, upload_to='files//%Y%m%d'),
        ),
        migrations.AlterField(
            model_name='report',
            name='file4',
            field=models.FileField(default=None, upload_to='files//%Y%m%d'),
        ),
        migrations.AlterField(
            model_name='report',
            name='file5',
            field=models.FileField(default=None, upload_to='files//%Y%m%d'),
        ),
    ]
