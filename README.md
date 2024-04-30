# 仕様技術一覧
- **Python**
- **React**
- **MySQL**
- **整備中**

# 環境
|言語フレームワーク等|バージョン|
|:---|:---:|
|Python|3.11.4|
|React||
|MySQL||
|サーバー||


# Python コーディング規約

## 超基礎的なコーディングルール
- ***スクリプトファイルの文字コードはUTF-8で作成する***
- ***行の先頭の空白は禁止***
- ***変数や関数などの表記法はスネークケースとする(例:all_sum,check_valid等)***

## コメントアウトについて
- ***関数は一つ一つにコメントアウトする***
- ***変数は使用する際の一つのまとまりごとにコメントアウトをする***
- ***一時的な変数や、ぱっと見分かる変数なら特にコメントアウトしなくてもいい***
---

## GitHubの管理について
- ***コミットは一つの機能ごとに分ける(検索機能・アカウント登録機能等)***

## コマンド一覧
### GitHubコマンド
|コマンド|説明|
|:--|:--|
|```git pull```|リモートのリポジトリからローカルにマージする|
|```git add [オプション]```|変更したものをローカルからステージングにあげる|
|```git commit -m [メッセージ]```|ステージングにあげたファイルの変更をコミットする（オプション-mを設定しない場合は、vimが起動してそこでメッセージを記載することとなる|
|```git push```|変更したファイル・ディレクトリをリモートリポジトリに反映させる|
|```git status```|変更されているファイルやステージングにあげられているファイル・ディレクトリの確認が出来る|
|```git merge [ブランチ名]```|現在のブランチにマージしたいブランチを選択する|
|```git checkout [オプション] [ブランチ名]```|移動したいブランチを選択する。オプションで-bを選択すると現在のブランチのコピーが新しいブランチにコピーされる|

## ローカル環境でのDjangoの動かし方
手順：
1\.　```pip install django``` ```pip install djangorestframework``` ```pip install django-environ```でdjango周りのインストールをする
<span style="color:red">(2~4は備忘録なので実施不要)</span>
2\.　```python -m django --version```でバージョン情報が出てくるか確認する
3\.　```django-admin startproject [プロジェクト名]```でプロジェクトを作成する
今回は既にchatAppディレクトリがあるので、プロジェクト名を適当に設定してもらい生成されたディレクトリ直下のmanage.pyとappディレクトリをコピーしてchatApp直下に配置する。そのあと[プロジェクト名]ディレクトリは削除する
4\.　```python manage.py startapp react_app``` ```python manage.py startapp api```でそれぞれ二つのディレクトリを作る
5\.　```python manage.py runserver```と入力し```localhost:8000/index```にアクセスし、以下の画面が表示されればOK！
![初回アクセスイメージ](https://github.com/kuriken121227/chatApp/assets/136247859/83363944-d3bd-42c1-8ae4-63006b45d594)

## MySQLの接続の仕方
手順:
1\. ```pip install mysqlclient```でmysql周りのインストールを行う
2\. .envファイルにデータベースの接続情報を設定する
3\. ```python manage.py migrate```を実行し以下の出力がされていればOK！
```Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying sessions.0001_initial... OK
```

## ER図 (修正中)
![super_er](https://github.com/kuriken121227/chatApp/assets/136247859/1d5b2e32-9296-4631-81a3-9dfcaa05f0d2)