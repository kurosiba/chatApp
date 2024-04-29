# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Chat(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True, db_comment='チャット識別用ID')  # Field name made lowercase.
    chatroomid = models.ForeignKey('Chatroom', models.DO_NOTHING, db_column='chatRoomID', db_comment='チャットルームID')  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='userID', db_comment='ユーザー識別用ID')  # Field name made lowercase.
    message = models.CharField(max_length=255, db_comment='メッセージ本文')
    sendtime = models.DateTimeField(db_comment='メッセージ送信時間')
    messagetype = models.IntegerField(db_column='messageType', db_comment='メッセージの種類')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'chat'
        db_table_comment = 'チャット情報'


class Chatroom(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True, db_comment='チャットルーム識別用ID')  # Field name made lowercase.
    roomname = models.CharField(max_length=255, db_comment='ルーム名')

    class Meta:
        managed = False
        db_table = 'chatroom'
        db_table_comment = 'チャットルーム'


class Conf(models.Model):
    user_id = models.ForeignKey('User', models.DO_NOTHING, db_column='ID', db_comment='設定識別用ID')  # Field name made lowercase.
    fontsize = models.IntegerField(db_column='fontSize', db_comment='フォントサイズ')  # Field name made lowercase.
    font = models.CharField(max_length=255, db_comment='フォント')
    noticeflg = models.IntegerField(db_column='noticeFlg', db_comment='通知フラグ')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'conf'
        db_table_comment = '設定情報'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Friend(models.Model):
    userid = models.OneToOneField('User', models.DO_NOTHING, db_column='userId', primary_key=True, db_comment='ユーザーID')  # Field name made lowercase. The composite primary key (userId, friendId) found, that is not supported. The first column is selected.
    friendid = models.ForeignKey('User', models.DO_NOTHING, db_column='friendId', related_name='friend_friendid_set', db_comment='フレンドID')  # Field name made lowercase.
    satisfieddate = models.DateTimeField(db_column='satisfiedDate', db_comment='フレンド成立日時')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'friend'
        unique_together = (('userid', 'friendid'),)
        db_table_comment = 'フレンド情報'


class Friendrequest(models.Model):
    applicantid = models.OneToOneField('User', models.DO_NOTHING, db_column='applicantId', primary_key=True, db_comment='申請者ID')  # Field name made lowercase. The composite primary key (applicantId, targetId) found, that is not supported. The first column is selected.
    targetid = models.ForeignKey('User', models.DO_NOTHING, db_column='targetId', related_name='friendrequest_targetid_set', db_comment='申請先ID')  # Field name made lowercase.
    applicantdate = models.DateTimeField(db_column='applicantDate', blank=True, null=True, db_comment='申請日時')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'friendrequest'
        unique_together = (('applicantid', 'targetid'),)
        db_table_comment = 'フレンド申請'


class Roominfo(models.Model):
    id = models.IntegerField(primary_key=True, db_comment='ルーム情報ID')
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='userid', db_comment='ユーザーID')
    chatroomid = models.ForeignKey(Chatroom, models.DO_NOTHING, db_column='chatroomid', db_comment='チャットルームID')

    class Meta:
        managed = False
        db_table = 'roominfo'
        db_table_comment = 'チャットルーム情報'


class User(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True, db_comment='ユーザ識別ID')  # Field name made lowercase.
    name = models.CharField(max_length=255, db_comment='ユーザー名')
    loginid = models.CharField(db_column='loginID', unique=True, max_length=255, db_comment='ログインID')  # Field name made lowercase.
    passwd = models.CharField(max_length=255, db_comment='ログインパスワード')
    lastlogin = models.DateTimeField(db_column='lastLogin', db_comment='最終ログイン')  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='createDate', db_comment='アカウント作成日時')  # Field name made lowercase.
    iconimage = models.CharField(db_column='iconImage', max_length=255, db_comment='アイコン画像パス')  # Field name made lowercase.
    confid = models.IntegerField(db_column='ConfID', db_comment='設定情報ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user'
        db_table_comment = 'ユーザマスタ'
