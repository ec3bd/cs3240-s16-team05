# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('secureshare', '0020_report_auth_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='auth_groups',
            field=models.ManyToManyField(to='auth.Group'),
        ),
    ]
