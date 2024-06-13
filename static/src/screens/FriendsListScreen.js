import React from 'react';
import { Link } from 'react-router-dom';

const FriendsListScreen = () => {
  return (
    <div>
      <div>My Profile</div>
      <div>------------フレンド一覧-------------</div>
      {/* フレンドリストを表示 */}
      <div>フレンド1</div>
      <div>フレンド2</div>
      <div>
        <Link to="/FriendsAdd">フレンド追加</Link>
      </div>
    </div>

  );
};

export default FriendsListScreen;