from django.db import IntegrityError, models
from django.forms import ValidationError
from django.utils import timezone

# Create your models here.

# ユーザー情報
class User(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True, db_comment='ユーザ識別ID')  # Field name made lowercase.
    name = models.CharField(max_length=255, db_comment='ユーザー名', default='')
    loginid = models.CharField(db_column='loginID', unique=True, max_length=255, db_comment='ログインID')  # Field name made lowercase.
    passwd = models.CharField(max_length=255, db_comment='ログインパスワード')
    lastlogin = models.DateTimeField(db_column='lastLogin', db_comment='最終ログイン', auto_now=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='createDate', db_comment='アカウント作成日時', auto_now_add=True)  # Field name made lowercase.
    iconimage = models.CharField(db_column='iconImage', max_length=255, db_comment='アイコン画像パス', default='icon/normal.png')  # Field name made lowercase.
    confid = models.IntegerField(db_column='ConfID', db_comment='設定情報ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user'
        db_table_comment = 'ユーザマスタ'

    def check_valid(self):
        #IDとパスワードが同じでないことの確認
        if self.loginid == self.passwd:
            raise ValidationError('IDとパスワードは同じものを設定することはできません')
            
    def save(self):
        try:
            self.check_valid()
        except ValidationError as e:
            raise e
        else:
            super().save()