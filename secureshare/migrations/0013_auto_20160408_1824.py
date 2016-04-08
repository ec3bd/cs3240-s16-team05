# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secureshare', '0012_auto_20160408_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='file1',
            field=models.FileField(upload_to='files//%Y%m%d'),
        ),
    ]
