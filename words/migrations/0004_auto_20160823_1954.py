# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0003_auto_20160819_1607'),
    ]

    operations = [
        migrations.CreateModel(
            name='WordRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('word_record', models.CharField(max_length=128, verbose_name=b'word')),
                ('is_correct', models.BooleanField(default=True, verbose_name=b'iscorrect')),
                ('correct_word', models.CharField(max_length=128, verbose_name=b'correct', blank=True)),
                ('word', models.ForeignKey(to='words.Word')),
                ('wordTest', models.ForeignKey(to='words.WordTest')),
            ],
            options={
                'verbose_name': 'word',
                'verbose_name_plural': 'words',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='word',
            name='correct_word',
        ),
        migrations.RemoveField(
            model_name='word',
            name='is_correct',
        ),
        migrations.RemoveField(
            model_name='word',
            name='test',
        ),
    ]
