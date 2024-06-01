from django.forms import ValidationError
from django.shortcuts import render
from .models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone
from django.db import IntegrityError
import json

# Create your views here.
# アカウント登録の処理
def regist_user(request):
    try:
        name = request.POST['name']
        id = request.POST['id']
        password = request.POST['password']
        user = User(name = name, loginid = id, passwd = password, confid = 0)
        user.save()
    except IntegrityError as e:
        # duplicate_error = 'このIDは既に利用されています。'
        return HttpResponse(status = 400)
    else:
        return HttpResponse(status = 200)