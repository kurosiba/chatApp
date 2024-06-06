# Generated by Django 5.0.4 on 2024-05-04 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fontsize', models.IntegerField(db_column='fontSize', db_comment='フォントサイズ')),
                ('font', models.CharField(db_comment='フォント', max_length=255)),
                ('noticeflg', models.IntegerField(db_column='noticeFlg', db_comment='通知フラグ')),
            ],
            options={
                'db_table': 'conf',
                'db_table_comment': '設定情報',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(db_column='ID', db_comment='ユーザ識別ID', primary_key=True, serialize=False)),
                ('name', models.CharField(db_comment='ユーザー名', max_length=255)),
                ('loginid', models.CharField(db_column='loginID', db_comment='ログインID', max_length=255, unique=True)),
                ('passwd', models.CharField(db_comment='ログインパスワード', max_length=255)),
                ('lastlogin', models.DateTimeField(db_column='lastLogin', db_comment='最終ログイン')),
                ('createdate', models.DateTimeField(db_column='createDate', db_comment='アカウント作成日時')),
                ('iconimage', models.CharField(db_column='iconImage', db_comment='アイコン画像パス', max_length=255)),
                ('confid', models.IntegerField(db_column='ConfID', db_comment='設定情報ID')),
            ],
            options={
                'db_table': 'user',
                'db_table_comment': 'ユーザマスタ',
                'managed': False,
            },
        ),
    ]