# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-01 17:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0002_auto_20181001_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenseclaim',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='expenseclaim',
            name='transactiondate',
            field=models.DateField(),
        ),
    ]
