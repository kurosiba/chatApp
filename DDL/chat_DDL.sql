--------------------------------------------------------------------------------
-- chat のレイアウト変更
--   注意！！：テーブルに依存するオブジェクト（ビューなど）が削除される場合があります。それらのオブジェクトは復元されません。
--   2024/04/25 kuri1
--------------------------------------------------------------------------------


-- 新テーブルの作成
create table if not exists chat (
  `ID` int not null auto_increment comment 'チャット識別用ID'
  , `chatRoomID` int not null comment 'チャットルームID'
  , `userID` int not null comment 'ユーザー識別用ID'
  , message varchar(255) not null comment 'メッセージ本文'
  , sendtime timestamp default CURRENT_TIMESTAMP not null comment 'メッセージ送信時間'
  , `messageType` int default 0 not null comment 'メッセージの種類'
  , primary key (`ID`)
)
  comment='チャット情報'
  engine InnoDB
  row_format DYNAMIC
  collate utf8mb3_general_ci;

-- 外部キーの作成
alter table chat
  add foreign key(userID) references user(ID);

alter table chat
  add foreign key(chatRoomID) references chatroom(ID);


