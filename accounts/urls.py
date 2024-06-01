from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path(r'user_list', views.user_list_view, name='user_list_view'),
    path(r'rgst_account', views.rgst_account, name='rgst_account')
]
