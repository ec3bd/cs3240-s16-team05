# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.TextField()),
                ('encrypt', models.BooleanField(default=False)),
                ('read', models.BooleanField(default=False)),
                ('receiver', models.ForeignKey(related_name='receiver', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(related_name='sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PasswordChange',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('oldPassword', models.CharField(max_length=100)),
                ('newPassword', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
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
                ('int_hash', models.CharField(max_length=100, default='')),
                ('auth_groups', models.ManyToManyField(to='auth.Group')),
                ('auth_users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('folders', models.ManyToManyField(to='secureshare.Folder')),
                ('owner', models.ForeignKey(related_name='owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UploadFile',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('file', models.FileField(upload_to='files/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('password2', models.CharField(max_length=100)),
                ('website', models.URLField(blank=True)),
                ('picture', models.ImageField(upload_to='profile_images', blank=True)),
                ('siteManager', models.BooleanField(default=False)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
