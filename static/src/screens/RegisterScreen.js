import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import './RegisterScreen.css';

const RegisterScreen = () => {
  const [userid, setUserid] = useState('');
  const [password, setPassword] = useState('');
  const [passwordConfirm, setPasswordConfirm] = useState('');
  const [username, setUsername] = useState('');
  const [duplicateError, setDuplicateError] = useState('');
  const [sameError, setSameError] = useState('');
  const [showPassword, setShowPassword] = useState(false);
  const navigate = useNavigate();

  const handleRegister = async (e) => {
    e.preventDefault();

    if (password !== passwordConfirm) {
      setSameError('Passwords do not match');
      return;
    }

    const response = await fetch('/api/regist_user', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCookie('csrftoken'),  // CSRFトークンを取得する関数を追加
      },
      body: JSON.stringify({
        userid,
        password,
        username
      }),
    });

    const data = await response.json();

    if (response.ok) {
      // 登録成功後の処理
      navigate('/login');
    } else {
      // 登録失敗時のエラーメッセージを設定
      if (data.duplicate_error) setDuplicateError(data.duplicate_error);
      if (data.same_error) setSameError(data.same_error);
    }
  };

  const togglePasswordVisibility = () => {
    setShowPassword(!showPassword);
  };

  // CSRFトークンを取得する関数（Djangoの場合）
  const getCookie = (name) => {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  };

  return (
    <div className="login-container">
      <div className="login-form">
        <h1 className="login-title">新規登録</h1>
        <form onSubmit={handleRegister}>
          <table>
            <tbody>
              <tr>
                <td className="input-group">
                  <label htmlFor="userId">ユーザーID</label>
                  <input
                    type="text"
                    id="userId"
                    value={userid}
                    onChange={(e) => setUserid(e.target.value)}
                    placeholder="ユーザーID"
                    required
                  />
                  {duplicateError && <span className="error-message">{duplicateError}</span>}
                </td>
              </tr>
              <tr>
                <td className="input-group">
                  <label htmlFor="password">パスワード</label>
                  <input
                    type={showPassword ? 'text' : 'password'}
                    id="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    placeholder="パスワード"
                    required
                  />
                  <i
                    className={`toggle-password fa ${showPassword ? 'fa-eye-slash' : 'fa-eye'}`}
                    onClick={togglePasswordVisibility}
                  ></i>
                </td>
              </tr>
              <tr>
                <td className="input-group">
                  <label htmlFor="passwordConfirm">確認用パスワード</label>
                  <input
                    type={showPassword ? 'text' : 'password'}
                    id="passwordConfirm"
                    value={passwordConfirm}
                    onChange={(e) => setPasswordConfirm(e.target.value)}
                    placeholder="確認用パスワード"
                    required
                  />
                  {sameError && <span className="error-message">{sameError}</span>}
                </td>
              </tr>
              <tr>
                <td className="input-group">
                  <label htmlFor="userName">ユーザ名</label>
                  <input
                    type="text"
                    id="userName"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    placeholder="ユーザ名"
                    required
                  />
                </td>
              </tr>
              <tr>
                <td>
                  <button type="submit" className="login-button">新規登録</button>
                </td>
              </tr>
            </tbody>
          </table>
        </form>
        <div className="register-link">
          <Link to="/login">既にアカウントをお持ちの方はこちら</Link>
        </div>
      </div>
    </div>
  );
};

export default RegisterScreen;
