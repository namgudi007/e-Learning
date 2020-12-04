# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-08 13:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_auto_20171008_1631'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default=1, max_length=1000)),
                ('file', models.FileField(default=1, upload_to='')),
                ('time', models.CharField(max_length=100)),
                ('deadline', models.CharField(max_length=100)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course')),
            ],
        ),
    ]