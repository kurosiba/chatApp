--------------------------------------------------------------------------------
-- `user` のレイアウト変更
--   注意！！：テーブルに依存するオブジェクト（ビューなど）が削除される場合があります。それらのオブジェクトは復元されません。
--   2024/04/25 kuri1
--------------------------------------------------------------------------------


-- 新テーブルの作成
create table if not exists user (
  `ID` int not null auto_increment comment 'ユーザ識別ID'
  , name varchar(255) not null comment 'ユーザー名'
  , `loginID` varchar(255) not null comment 'ログインID' UNIQUE
  , passwd varchar(255) not null comment 'ログインパスワード'
  , `lastLogin` timestamp default CURRENT_TIMESTAMP not null comment '最終ログイン'
  , `createDate` timestamp default CURRENT_TIMESTAMP not null comment 'アカウント作成日時'
  , `iconImage` varchar(255) default 'icon/normal.png' not null comment 'アイコン画像パス'
  , `ConfID` int not null comment '設定情報ID'
  , primary key (`ID`)
)
  comment='ユーザマスタ'
  engine InnoDB
  row_format DYNAMIC
  collate utf8mb3_general_ci;