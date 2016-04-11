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
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('docfile', models.FileField(upload_to='documents/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='GroupPage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('url', models.URLField(blank=True)),
                ('group', models.OneToOneField(to='auth.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('oldPassword', models.CharField(max_length=100)),
                ('newPassword', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created_at', models.TextField()),
                ('short_description', models.CharField(max_length=200)),
                ('detailed_description', models.TextField()),
                ('file1', models.FileField(null=True, upload_to='files/%Y%m%d')),
                ('file2', models.FileField(null=True, upload_to='files/%Y%m%d')),
                ('file3', models.FileField(null=True, upload_to='files/%Y%m%d')),
                ('file4', models.FileField(null=True, upload_to='files/%Y%m%d')),
                ('file5', models.FileField(null=True, upload_to='files/%Y%m%d')),
                ('private', models.BooleanField(default=False)),
                ('encrypt', models.BooleanField(default=False)),
                ('auth_groups', models.ManyToManyField(to='auth.Group')),
                ('auth_users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(related_name='owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UploadFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('file', models.FileField(upload_to='files/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('website', models.URLField(blank=True)),
                ('picture', models.ImageField(blank=True, upload_to='profile_images')),
                ('siteManager', models.BooleanField(default=False)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
