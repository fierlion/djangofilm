# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200, null=True, blank=True)),
                ('movielength', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Theater',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('chambers', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='theater',
            field=models.ForeignKey(to='movielib.Theater', null=True),
        ),
    ]
