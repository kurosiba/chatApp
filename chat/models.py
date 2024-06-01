# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from room.models import Roominfo
from accounts.models import User


class Chat(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True, db_comment='チャット識別用ID')  # Field name made lowercase.
    chatroomid = models.ForeignKey(Roominfo, models.DO_NOTHING, db_column='chatRoomID', db_comment='チャットルームID')  # Field name made lowercase.
    userid = models.ForeignKey(User, models.DO_NOTHING, db_column='userID', db_comment='ユーザー識別用ID')  # Field name made lowercase.
    message = models.CharField(max_length=255, db_comment='メッセージ本文')
    sendtime = models.DateTimeField(db_comment='メッセージ送信時間')
    messagetype = models.IntegerField(db_column='messageType', db_comment='メッセージの種類')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'chat'
        db_table_comment = 'チャット情報'