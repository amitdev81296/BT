# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-19 06:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Verb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verb', models.CharField(max_length=30)),
                ('category', models.CharField(choices=[('Creating', 'Creating'), ('Evaluating', 'Evaluating'), ('Analyzing', 'Analyzing'), ('Applying', 'Applying'), ('Understanding', 'Understanding'), ('Remembering', 'Remembering')], max_length=20)),
            ],
        ),
    ]
