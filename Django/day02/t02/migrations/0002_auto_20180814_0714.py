# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-14 07:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('t02', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='firecart',
            options={'verbose_name': ('火车类',)},
        ),
        migrations.AlterField(
            model_name='firecart',
            name='speed',
            field=models.IntegerField(db_column='my_speed', default=300, verbose_name='时速'),
        ),
        migrations.AlterModelTable(
            name='firecart',
            table='huocart',
        ),
    ]
