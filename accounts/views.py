# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from accounts.forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import update_session_auth_hash
from accounts.models import UserProfile
from expense.models import ExpenseClaim
# Create your views here.
def logout(request):
    args = {
            'useractive': "false",
            }
    return render(request,'accounts/home.html',args)
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
    msg = []
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print "valid"
            form.save()
            return redirect('/account/login')
        else:
            form = RegistrationForm()
            # username taken
            if User.objects.filter(username=request.POST['username']).exists():
                msg.append("username Exist")
            # used email address
            if User.objects.filter(email=request.POST['email']).exists():
                msg.append("Email Address Exist")
            # different password
            if request.POST['password1'] != request.POST['password2']:
                msg.append("Your password and confirmation password do not match.")
            # password requirement
            if len(request.POST['password1']) < 8 or len(request.POST['password2']) < 8:
                msg.append("Password must be more than 8 characters")
            elif request.POST['password1'].isdigit() or request.POST['password2'].isdigit():
                msg.append("Password must not be only integer")
            
            args = {'form': form,'msg': msg,
            'msgtrue': "true",'alerttype':'danger',}
            return render(request, 'accounts/reg_form.html',args)

    else:
        form = RegistrationForm()

        args = {'form': form,
        'useractive': 'false',
        }
        return render(request, 'accounts/reg_form.html',args)

def view_profile(request):
    if request.user.is_authenticated == True:
        name = request.user
        useractive = "true" 
    else:
        name = ""
        useractive = "false"
    if request.user.is_superuser:
        superuser = "true"
    else:
        superuser = "false"
    MyExpenseClaim =ExpenseClaim.objects.filter(user__id=request.user.id)

    args = {'superuser': superuser,'user': request.user,
            'myname': request.user,
            'useractive': useractive,
            'myclaim': MyExpenseClaim}
    return render(request,'accounts/profile.html',args)

