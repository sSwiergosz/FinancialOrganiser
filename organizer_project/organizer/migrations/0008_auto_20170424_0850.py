# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-24 06:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0007_auto_20170424_0822'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='organizer.Category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('APP/ACC', 'Apparel/Accesory'), ('ENT', 'Entertainment'), ('F/B', 'Food/Beverage'), ('SC/C', 'Skin care/Cosmetics'), ('C/M', 'Computer/Mobile'), ('B/N', 'Books/Newspapers')], default='APP/ACC', max_length=30),
        ),
    ]
