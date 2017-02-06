# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-06 18:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Kasha', '0004_source_questions_listing'),
    ]

    operations = [
        migrations.CreateModel(
            name='SourceQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_chapter_sentence', models.CharField(max_length=100)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Kasha.Question')),
            ],
        ),
        migrations.DeleteModel(
            name='Source_Questions_Listing',
        ),
    ]
