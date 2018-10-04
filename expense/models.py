# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from expense.choices import *
from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Create your models here.
class ExpenseClaim(models.Model):
    name = models.CharField(max_length=50)
    branchcode = models.CharField(max_length=15)
    date = models.DateField(auto_now_add=True, blank=True)
    bankcode = models.CharField(
        max_length=100,
        choices=BANK_CODE,
        null=True
    )
    bankacc = models.IntegerField()
    bankaccname = models.CharField(max_length=50)
    transactiondate = models.DateField()
    costcenter = models.CharField(max_length=10)
    glcode = models.CharField(
        max_length=100,
        choices=GL_CODE,
        null=True
    )
    description = models.CharField(max_length=150)
    currency = models.CharField(max_length=2,default="RM")
    amount = models.IntegerField()
    user = models.ForeignKey(User)

