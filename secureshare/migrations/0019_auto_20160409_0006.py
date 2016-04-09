# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secureshare', '0018_auto_20160408_1836'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Document',
        ),
        migrations.DeleteModel(
            name='UploadFile',
        ),
        migrations.AddField(
            model_name='message',
            name='read',
            field=models.BooleanField(default=False),
        ),
    ]
