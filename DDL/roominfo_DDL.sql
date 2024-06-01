--------------------------------------------------------------------------------
-- roominfo のレイアウト変更
--   注意！！：テーブルに依存するオブジェクト（ビューなど）が削除される場合があります。それらのオブジェクトは復元されません。
--   2024/04/25 kuri1
--------------------------------------------------------------------------------


-- 新テーブルの作成
create table if not exists roominfo (
  id int not null comment 'ルーム情報ID'
  , userid int not null comment 'ユーザーID'
  , chatroomid int not null comment 'チャットルームID'
  , primary key (id)
)
  comment='チャットルーム情報'
  engine InnoDB
  row_format DYNAMIC
  collate utf8mb3_general_ci;

-- 外部キーの作成
alter table roominfo
    add foreign key(userid) references user(ID);


alter table roominfo
    add foreign key(chatroomid) references chatroom(ID);


