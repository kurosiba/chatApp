import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import './LoginScreen.css'; // CSSファイルをインポート

const LoginScreen = () => {
  const [userId, setUserId] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleLogin = (e) => {
    e.preventDefault();
    // ログイン処理
    console.log('Login attempt with:', userId, password);
    navigate('/friends'); // ログイン成功時にフレンドリストスクリーンに遷移
  };

  return (
    <div className="login-container">
      <div className="login-form">
        <h1 className="login-title">ログイン</h1>
        <form onSubmit={handleLogin}>
          <div className="input-group">
            <label htmlFor="userId">ユーザーID</label>
            <input
              id="userId"
              type="text"
              value={userId}
              onChange={(e) => setUserId(e.target.value)}
              required
              placeholder="ユーザーID" 
            />
          </div>
          <div className="input-group">
            <label htmlFor="password">パスワード</label>
            <input
              id="password"
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
              placeholder="パスワード" 
            />
          </div>
          <button type="submit" className="login-button">ログイン</button>
        </form>
        <div className="register-link">
          <Link to="/register">新規登録はこちら</Link>
        </div>
      </div>
    </div>
  );
};

export default LoginScreen;
