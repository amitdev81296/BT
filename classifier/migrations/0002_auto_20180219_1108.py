# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-19 05:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classifier', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=b'')),
            ],
        ),
        migrations.DeleteModel(
            name='Verb',
        ),
    ]