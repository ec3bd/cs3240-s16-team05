# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secureshare', '0010_grouppage'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='encrypt',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='report',
            name='file1',
            field=models.FileField(default=None, upload_to=''),
        ),
        migrations.AddField(
            model_name='report',
            name='file2',
            field=models.FileField(default=None, upload_to=''),
        ),
        migrations.AddField(
            model_name='report',
            name='file3',
            field=models.FileField(default=None, upload_to=''),
        ),
        migrations.AddField(
            model_name='report',
            name='file4',
            field=models.FileField(default=None, upload_to=''),
        ),
        migrations.AddField(
            model_name='report',
            name='file5',
            field=models.FileField(default=None, upload_to=''),
        ),
    ]
