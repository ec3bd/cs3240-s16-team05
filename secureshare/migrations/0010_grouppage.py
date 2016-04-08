# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('secureshare', '0009_auto_20160406_1419'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupPage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('url', models.URLField(blank=True)),
                ('group', models.OneToOneField(to='auth.Group')),
            ],
        ),
    ]
