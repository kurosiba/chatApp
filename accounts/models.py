# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.utils import timezone

# ユーザー情報
class User(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True, db_comment='ユーザ識別ID')  # Field name made lowercase.
    name = models.CharField(max_length=255, db_comment='ユーザー名')
    loginid = models.CharField(db_column='loginID', unique=True, max_length=255, db_comment='ログインID')  # Field name made lowercase.
    passwd = models.CharField(max_length=255, db_comment='ログインパスワード')
    lastlogin = models.DateTimeField(db_column='lastLogin', db_comment='最終ログイン', default=timezone.now)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='createDate', db_comment='アカウント作成日時', auto_now_add=True)  # Field name made lowercase.
    iconimage = models.CharField(db_column='iconImage', max_length=255, db_comment='アイコン画像パス', default='icon/normal.png')  # Field name made lowercase.
    confid = models.IntegerField(db_column='ConfID', db_comment='設定情報ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user'
        db_table_comment = 'ユーザマスタ'


# 設定情報
class Conf(models.Model):
    user_id = models.ForeignKey('User', models.DO_NOTHING, db_column='ID', db_comment='設定識別用ID')  # Field name made lowercase.
    fontsize = models.IntegerField(db_column='fontSize', db_comment='フォントサイズ')  # Field name made lowercase.
    font = models.CharField(max_length=255, db_comment='フォント')
    noticeflg = models.IntegerField(db_column='noticeFlg', db_comment='通知フラグ')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'conf'
        db_table_comment = '設定情報'

        
