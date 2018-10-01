# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from expense.forms import ExpenseClaimForm
from django.shortcuts import render, redirect
from expense.models import ExpenseClaim

# Create your views here.

def ExpenseClaims(request):
    if request.user.is_authenticated != True:
        return redirect('/account/')
    if request.user.is_superuser:
        superuser = "true"
    else:
        superuser = "false"
    if request.method == 'POST':
            form = ExpenseClaimForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.user = request.user
                post.save()
                args ={'user': request.user,
            'myname': request.user,
            'useractive': "true",
            'msg': "Expense claim has been created successfully",
            'msgtrue': "true"}
                
                return render(request, 'accounts/profile.html',args)
            else:
                form = ExpenseClaimForm()

                args = {'form': form}
                return redirect('/expense/')
    else:
        form = ExpenseClaimForm()

        args = {'form': form,
        'superuser': superuser,
        'myname': request.user,
            'useractive': "true",}
        return render(request, 'expense/claim_form.html',args)

def ExpenseList(request):
    if not request.user.is_superuser:
        return redirect('/account/')
    ExpenseClaimList = ExpenseClaim.objects.order_by('date')
    args = {
    'expensedata': ExpenseClaimList,
    'myname': request.user,
            'useractive': "true",}
    
    return render(request, 'expense/claim_list.html',args)