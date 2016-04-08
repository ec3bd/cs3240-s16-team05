# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secureshare', '0011_auto_20160408_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='file1',
            field=models.FileField(default=None, upload_to='', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='file2',
            field=models.FileField(default=None, upload_to='', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='file3',
            field=models.FileField(default=None, upload_to='', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='file4',
            field=models.FileField(default=None, upload_to='', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='file5',
            field=models.FileField(default=None, upload_to='', null=True, blank=True),
        ),
    ]
