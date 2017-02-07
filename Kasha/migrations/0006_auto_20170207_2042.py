# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-07 20:42
from __future__ import unicode_literals

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Kasha', '0005_auto_20170206_1859'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookChapterQuestions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=100)),
                ('chapter', models.CharField(max_length=100)),
                ('question_list', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'Question', 'verbose_name_plural': 'Questions'},
        ),
        migrations.AddField(
            model_name='question',
            name='tags',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, default=['genesis.1.1'], size=None),
            preserve_default=False,
        ),
    ]
