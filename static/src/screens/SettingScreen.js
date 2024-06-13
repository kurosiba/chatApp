import React, { useContext, useState } from 'react';
import FontContext from './FontContext';

const SettingsForm = () => {
  const [fontSize, setFontSize] = useState('medium');
  const [notification, setNotification] = useState('enabled');
  // コンテキストから font と setFont を取得
  const { font, setFont } = useContext(FontContext); 

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(`Settings: Font Size - ${fontSize}, Font - ${font}, Notifications - ${notification}`);
    // 設定保存処理はここで行う
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label>
          文字サイズ:
          <select value={fontSize} onChange={(e) => setFontSize(e.target.value)}>
            <option value="small">小</option>
            <option value="medium">中</option>
            <option value="large">大</option>
          </select>
        </label>
      </div>
      <div>
        <label>
          フォント:
          <select value={font} onChange={(e) => setFont(e.target.value)}>
            <option value="游明朝">游明朝</option>
            <option value="ゴシック">ゴシック</option>
          </select>
        </label>
      </div>
      <div>
        <label>
          通知:
          <select value={notification} onChange={(e) => setNotification(e.target.value)}>
            <option value="enabled">ON</option>
            <option value="disabled">OFF</option>
          </select>
        </label>
      </div>
      <button type="submit">適用</button>
    </form>
  );
};

export default SettingsForm;
