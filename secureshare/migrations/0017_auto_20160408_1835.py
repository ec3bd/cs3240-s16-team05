# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('secureshare', '0016_auto_20160408_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='file1',
            field=models.FileField(default=False, upload_to='files/%Y%m%d'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='report',
            name='file2',
            field=models.FileField(default=datetime.datetime(2016, 4, 8, 22, 34, 45, 468320, tzinfo=utc), upload_to='files/%Y%m%d'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='report',
            name='file3',
            field=models.FileField(default=datetime.datetime(2016, 4, 8, 22, 34, 58, 616426, tzinfo=utc), upload_to='files/%Y%m%d'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='report',
            name='file4',
            field=models.FileField(default=datetime.datetime(2016, 4, 8, 22, 35, 3, 263269, tzinfo=utc), upload_to='files/%Y%m%d'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='report',
            name='file5',
            field=models.FileField(default=datetime.datetime(2016, 4, 8, 22, 35, 8, 145236, tzinfo=utc), upload_to='files/%Y%m%d'),
            preserve_default=False,
        ),
    ]
