# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from api.accounts.models import User


class Friend(models.Model):
    userid = models.OneToOneField(User, models.DO_NOTHING, db_column='userId', primary_key=True, db_comment='ユーザーID')  # Field name made lowercase. The composite primary key (userId, friendId) found, that is not supported. The first column is selected.
    friendid = models.ForeignKey(User, models.DO_NOTHING, db_column='friendId', related_name='friend_friendid_set', db_comment='フレンドID')  # Field name made lowercase.
    satisfieddate = models.DateTimeField(db_column='satisfiedDate', db_comment='フレンド成立日時')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'friend'
        unique_together = (('userid', 'friendid'),)
        db_table_comment = 'フレンド情報'


class Friendrequest(models.Model):
    applicantid = models.OneToOneField(User, models.DO_NOTHING, db_column='applicantId', primary_key=True, db_comment='申請者ID')  # Field name made lowercase. The composite primary key (applicantId, targetId) found, that is not supported. The first column is selected.
    targetid = models.ForeignKey(User, models.DO_NOTHING, db_column='targetId', related_name='friendrequest_targetid_set', db_comment='申請先ID')  # Field name made lowercase.
    applicantdate = models.DateTimeField(db_column='applicantDate', blank=True, null=True, db_comment='申請日時')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'friendrequest'
        unique_together = (('applicantid', 'targetid'),)
        db_table_comment = 'フレンド申請'