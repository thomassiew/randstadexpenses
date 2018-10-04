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
    MyExpenseClaim =ExpenseClaim.objects.filter(user__id=request.user.id)
    if request.method == 'POST':
            form = ExpenseClaimForm(request.POST)
            
            if form.is_valid():
                print "hi"
                post = form.save(commit=False)
                post.user = request.user
                post.name = request.user.username
                
                post.save()
                args ={'form': form,'user': request.user,
            'myname': request.user,
            'useractive': "true",
            'msg': "Expense claim has been created successfully",
            'msgtrue': "true",
            'alerttype':'success','superuser': superuser,'myclaim': MyExpenseClaim,}
                
                return render(request, 'expense/claim_form.html',args)
            else:
                msg = form.errors
                
                form = ExpenseClaimForm()

                args = {'form': form,'msg': msg,'myclaim': MyExpenseClaim,
        'msgtrue': "true",'alerttype':'danger','superuser': superuser,}
                return render(request, 'expense/claim_form.html',args)
    else:
        form = ExpenseClaimForm()

        args = {'form': form,
        'superuser': superuser,
        'myname': request.user,
        'myclaim': MyExpenseClaim,
            'useractive': "true",}
        return render(request, 'expense/claim_form.html',args)

def ExpenseList(request):
    if not request.user.is_superuser:
        return redirect('/account/')
    ExpenseClaimList = ExpenseClaim.objects.order_by('date')
    args = {
    'expensedata': ExpenseClaimList,
    'myname': request.user,
            'useractive': "true",'superuser': "true",}
    
    return render(request, 'expense/claim_list.html',args)