# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from accounts.forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import update_session_auth_hash
from expense.models import ExpenseClaim
# Create your views here.
def home(request):
    if request.user.is_authenticated == True:
        name = request.user
        useractive = "true" 
        return redirect('/expense')
    else:
        name = ""
        useractive = "false"
    args = {'myname': name,
            'useractive': useractive,
            }
    return render(request,'accounts/home.html',args)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account/login')
        else:
            form = RegistrationForm()

            args = {'form': form}
            return render(request, 'accounts/reg_form.html',args)

    else:
        form = RegistrationForm()

        args = {'form': form,
        'useractive': 'false'}
        return render(request, 'accounts/reg_form.html',args)

def view_profile(request):
    if request.user.is_authenticated == True:
        name = request.user
        useractive = "true" 
    else:
        name = ""
        useractive = "false"

    MyExpenseClaim =ExpenseClaim.objects.filter(user__id=request.user.id)

    args = {'user': request.user,
            'myname': request.user,
            'useractive': useractive,
            'myclaim': MyExpenseClaim}
    return render(request,'accounts/profile.html',args)

