from .models import User
from django.db import IntegrityError
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
# アカウント登録の処理
@api_view(['POST'])
def regist_user(request):
    try:
        name = request.data.get("name")
        id = request.data.get("id")
        passwd = request.data.get("passwd")
        user = User(name = name, loginid = id, passwd = passwd, confid = 0)
        user.save()
    except IntegrityError as e:
        # duplicate_error = 'このIDは既に利用されています。'
        print(e)
        return Response(status = status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status = status.HTTP_200_OK)

# ログイン処理
@api_view(['POST'])
def check_login(request):
    try:
        id = request.data.get("id")
        passwd = request.data.get("passwd")
        # idとパスワードでDB検索
        # 一件しか取れない想定なのでgetを使用
        login_user = User.objects.get(loginid = id, passwd = passwd)
    except Exception as e:
        print(e)
        return Response(status = status.HTTP_400_BAD_REQUEST)
    else:
        #Jsonの作成
        user_id = { "ID" : login_user.id }
        return Response(user_id, status.HTTP_200_OK)