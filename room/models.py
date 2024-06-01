# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from accounts.models import User


class Chatroom(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True, db_comment='チャットルーム識別用ID')  # Field name made lowercase.
    roomname = models.CharField(max_length=255, db_comment='ルーム名')

    class Meta:
        managed = False
        db_table = 'chatroom'
        db_table_comment = 'チャットルーム'


class Roominfo(models.Model):
    id = models.IntegerField(primary_key=True, db_comment='ルーム情報ID')
    userid = models.ForeignKey(User, models.DO_NOTHING, db_column='userid', db_comment='ユーザーID')
    chatroomid = models.ForeignKey(Chatroom, models.DO_NOTHING, db_column='chatroomid', db_comment='チャットルームID')

    class Meta:
        managed = False
        db_table = 'roominfo'
        db_table_comment = 'チャットルーム情報'