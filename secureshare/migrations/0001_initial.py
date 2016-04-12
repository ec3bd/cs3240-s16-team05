# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupPage',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('url', models.URLField(blank=True)),
                ('group', models.OneToOneField(to='auth.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.TextField()),
                ('encrypt', models.BooleanField(default=False)),
                ('read', models.BooleanField(default=False)),
                ('receiver', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='receiver')),
                ('sender', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='sender')),
            ],
        ),
        migrations.CreateModel(
            name='PasswordChange',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('oldPassword', models.CharField(max_length=100)),
                ('newPassword', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('created_at', models.TextField()),
                ('short_description', models.CharField(max_length=200)),
                ('detailed_description', models.TextField()),
                ('file1', models.FileField(upload_to='files/%Y%m%d', null=True)),
                ('file2', models.FileField(upload_to='files/%Y%m%d', null=True)),
                ('file3', models.FileField(upload_to='files/%Y%m%d', null=True)),
                ('file4', models.FileField(upload_to='files/%Y%m%d', null=True)),
                ('file5', models.FileField(upload_to='files/%Y%m%d', null=True)),
                ('private', models.BooleanField(default=False)),
                ('encrypt', models.BooleanField(default=False)),
                ('int_hash', models.CharField(default='', max_length=100)),
                ('auth_groups', models.ManyToManyField(to='auth.Group')),
                ('auth_users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='owner')),
            ],
        ),
        migrations.CreateModel(
            name='UploadFile',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('file', models.FileField(upload_to='files/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('password2', models.CharField(max_length=100)),
                ('random', models.CharField(max_length=100)),
                ('website', models.URLField(blank=True)),
                ('picture', models.ImageField(blank=True, upload_to='profile_images')),
                ('siteManager', models.BooleanField(default=False)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
