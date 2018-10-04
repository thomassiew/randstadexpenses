# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-04 17:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0007_auto_20181004_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenseclaim',
            name='glcode',
            field=models.CharField(choices=[(b'4165', b'Staff Reimbursement Mobile'), (b'4190', b'Postage'), (b'4191', b'Couriers'), (b'4200', b'Stationery'), (b'4311', b'International Fares'), (b'4312', b'Internation Accomodation'), (b'4313', b'International Expense'), (b'4321', b'Local Fares')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='expenseclaim',
            name='transactiondate',
            field=models.DateField(),
        ),
    ]
