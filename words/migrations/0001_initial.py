# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-19 15:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=128, verbose_name='word')),
                ('is_correct', models.BooleanField(default=True, verbose_name='iscorrect')),
                ('correct_word', models.CharField(max_length=128, verbose_name='correct')),
            ],
            options={
                'verbose_name_plural': 'words',
                'verbose_name': 'word',
            },
        ),
        migrations.CreateModel(
            name='WordTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_date', models.DateTimeField(auto_now_add=True, verbose_name='testdate')),
                ('count', models.DecimalField(decimal_places=0, default=50, max_digits=3, verbose_name='count')),
            ],
            options={
                'verbose_name_plural': 'Tests',
                'verbose_name': 'Test',
                'ordering': ['test_date'],
            },
        ),
        migrations.AddField(
            model_name='word',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='words.WordTest'),
        ),
    ]
