# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-04 17:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0004_auto_20181001_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenseclaim',
            name='bankcode',
            field=models.CharField(choices=[(1, b'ARBKMYKL AmBank'), (1, b'DEUTMYKL Deutsche Bank'), (1, b'PBBEMYKL Public Bank'), (1, b'HBMBMYKL HSBC Bank'), (1, b'MFBBMYKL Maybank'), (2, b'CIBBMYKL CIMB bank'), (1, b'UOVBMYKL UOB Bank'), (3, b'HLBBMYKL Hong Leong bank'), (1, b'OCBCMYKL OCBC Bank'), (1, b'RHBBMYKL RHB Bank')], max_length=1),
        ),
        migrations.AlterField(
            model_name='expenseclaim',
            name='glcode',
            field=models.CharField(choices=[(1, b'4165 Staff Reimbursement Mobile'), (2, b'4190 Postage'), (3, b'4191 Couriers'), (4, b'4200 Stationery'), (5, b'4311 International Fares'), (6, b'4312 Internation Accomodation'), (7, b'4313 International Expense'), (8, b'4321 Local Fares')], max_length=1),
        ),
    ]