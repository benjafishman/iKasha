# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-10 18:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Kasha', '0010_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Kasha.Question'),
            preserve_default=False,
        ),
    ]
