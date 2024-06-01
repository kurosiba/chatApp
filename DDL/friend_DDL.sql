--------------------------------------------------------------------------------
-- friend のレイアウト変更
--   注意！！：テーブルに依存するオブジェクト（ビューなど）が削除される場合があります。それらのオブジェクトは復元されません。
--   2024/04/25 kuri1
--------------------------------------------------------------------------------


-- 新テーブルの作成
create table if not exists friend (
  `userId` INT not null comment 'ユーザーID'
  , `friendId` INT not null comment 'フレンドID'
  , `satisfiedDate` TIMESTAMP not null comment 'フレンド成立日時'
  , primary key (`userId`,`friendId`)
)
  comment='フレンド情報'
  engine InnoDB
  row_format DYNAMIC;

-- 外部キーの作成
alter table friend
    add foreign key(userId) references user(ID);
    
alter table friend
    add foreign key(friendId) references user(ID);
