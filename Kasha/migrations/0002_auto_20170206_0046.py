# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-06 00:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kasha', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='en_verse_text',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='question',
            name='he_verse_text',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.TextField(max_length=500),
        ),
    ]
