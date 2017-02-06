# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-05 20:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=500)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('he_verse_text', models.CharField(max_length=500)),
                ('en_verse_text', models.CharField(max_length=500)),
                ('book_source', models.CharField(max_length=500)),
            ],
        ),
    ]