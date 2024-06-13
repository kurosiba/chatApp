//FriendsAddScreen
import React, { useState } from 'react';
import styles from './FriendsAddScreen.css';

const SearchForm = () => {
  const [searchType, setSearchType] = useState('userId'); // 検索タイプの状態
  const [searchQuery, setSearchQuery] = useState(''); // 検索クエリの状態

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(`Searching for ${searchQuery} by ${searchType}`);
    // ここで検索処理を実装。例: APIへのリクエストを送るなど。
  };

  return (
    <form onSubmit={handleSubmit} className={styles.searchForm}>
      <h1 className="friendsAdd-title">フレンド追加</h1>
      <div className={styles.searchInputGroup}>
        <label>
          <input
            type="radio"
            value="userId"
            checked={searchType === 'userId'}
            onChange={(e) => setSearchType(e.target.value)}
          />
          ユーザID
        </label>
        <label>
          <input
            type="radio"
            value="username"
            checked={searchType === 'username'}
            onChange={(e) => setSearchType(e.target.value)}
          />
          ユーザ名
        </label>
      </div>
      <div className={styles.searchInputGroup}>
        <input
          type="text"
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
          placeholder="検索クエリ"
          className={styles.searchInput}
        />
        <button type="submit" className={styles.searchButton}>検索</button>
      </div>
    </form>
  );
};

export default SearchForm;