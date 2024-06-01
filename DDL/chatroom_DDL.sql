--------------------------------------------------------------------------------
-- chatroom のレイアウト変更
--   注意！！：テーブルに依存するオブジェクト（ビューなど）が削除される場合があります。それらのオブジェクトは復元されません。
--   2024/04/25 kuri1
--------------------------------------------------------------------------------


-- 新テーブルの作成
create table if not exists chatroom (
  `ID` int not null auto_increment comment 'チャットルーム識別用ID'
  , roomname varchar(255) not null comment 'ルーム名'
  , primary key (`ID`)
)
  comment='チャットルーム'
  engine InnoDB
  row_format DYNAMIC
  collate utf8mb3_general_ci;