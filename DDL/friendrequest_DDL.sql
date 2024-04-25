--------------------------------------------------------------------------------
-- friendrequest のレイアウト変更
--   注意！！：テーブルに依存するオブジェクト（ビューなど）が削除される場合があります。それらのオブジェクトは復元されません。
--   2024/04/25 kuri1
--------------------------------------------------------------------------------


-- 新テーブルの作成
create table if not exists friendrequest (
  applicantId INT not null comment '申請者ID'
  , targetId INT not null comment '申請先ID'
  , applicantDate TIMESTAMP default current_timestamp comment '申請日時'
  , primary key (applicantId,targetId)
)
  comment='フレンド申請'
  engine InnoDB
  row_format DYNAMIC;

-- 外部キーの作成
alter table friendrequest
    add foreign key(applicantId) references user(ID);

alter table friendrequest
    add foreign key(targetId) references user(ID);
    


