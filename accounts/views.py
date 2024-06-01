from django.shortcuts import render
from .models import User, Conf
from django.http import HttpResponse
import json

# Create your views here.
def user_list_view(request):
    # Userテーブルから全レコードの取得
    user_list = User.objects.all()

    if user_list.count() == 0:
        return HttpResponse('Not exists data')
    else:
        users = list(user_list.values('id', 'name', 'passwd'))
        users_json = json.dumps(users, indent=3)
        print(users_json)
        return HttpResponse(users_json)