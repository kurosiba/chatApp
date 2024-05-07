from django.shortcuts import render
from .models import User
from django.http import HttpResponseRedirect
from django.utils import timezone
import json

# Create your views here.
def regist_user(request):
    name = request.POST['name']
    id = request.POST['id']
    password = request.POST['password']
    user = User(name = name, loginid = id, passwd = password, confid = 0)
    user.save()
    return HttpResponseRedirect('/accounts/rgst_account')
