--------------------------------------------------------------------------------
-- conf のレイアウト変更
--   注意！！：テーブルに依存するオブジェクト（ビューなど）が削除される場合があります。それらのオブジェクトは復元されません。
--   2024/04/25 kuri1
--------------------------------------------------------------------------------


-- 新テーブルの作成
create table if not exists conf (
  `ID` int not null comment '設定識別用ID'
  , `fontSize` int default 10 not null comment 'フォントサイズ'
  , font varchar(255) default 'ゴシック' not null comment 'フォント'
  , `noticeFlg` tinyint(1) default 1 not null comment '通知フラグ'
)
  comment='設定情報'
  engine InnoDB
  row_format DYNAMIC
  collate utf8mb3_general_ci;


--外部キー設定
alter table conf
  add foreign key(ID) references user(ID);

