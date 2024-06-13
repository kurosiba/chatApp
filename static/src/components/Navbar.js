// Navbar.js
// 画面下部に表示されるナビゲーションバー

import React from 'react';
import { NavLink } from 'react-router-dom';
import './Navbar.css'; // スタイルシートのインポート

//アイコン配置
import friendsListIcon from '../assets/images/HomeIcon.png';
import friendsInactiveIcon from '../assets/images/HomeIconOn.png';
import talksListIcon from '../assets/images/TalkIcon.png';
import talksInactiveIcon from '../assets/images/TalkIconOn.png';
import settingsIcon from '../assets/images/SettingIcon.png';
import settingsInactiveIcon from '../assets/images/SettingIconOn.png';
import dog from '../assets/images/dog.gif';

const Navbar = () => {
  return (
<div className="navbar">
      <NavLink to="/friends" activeClassName="active">
        <img src={friendsInactiveIcon} alt="フレンド一覧" className="inactive" style={{width: '56px', height: 'auto' }}/>
        <img src={friendsListIcon} alt="フレンド一覧" className="active" style={{width: '56px', height: 'auto' }}/>
      </NavLink>
      <NavLink to="/talkslist" activeClassName="active">
        <img src={talksInactiveIcon} alt="トーク一覧" className="inactive" style={{width: '56px', height: 'auto' }}/>
        <img src={talksListIcon} alt="トーク一覧" className="active" style={{width: '56px', height: 'auto' }}/>
      </NavLink>
      <NavLink to="/Setting" activeClassName="active">
        <img src={settingsInactiveIcon} alt="設定" className="inactive" style={{width: '56px', height: 'auto' }}/>
        <img src={settingsIcon} alt="設定" className="active" style={{width: '56px', height: 'auto' }}/>
      </NavLink>
      <NavLink to="/" activeClassName="active" className="logout-link">
        <img src={dog} alt="logout" style={{width: '56px', height: 'auto' }}/>
      </NavLink>
    </div>
  );
};

//
export default Navbar;

// 　　　 ／⌒ヽ
// 　　 ／　　　＼
// 　　/　　　 丶 ＼
// 　 (/　　　　丶　)
// 　 /　　　　　丶”
// 　f ー　　ー　 i
// 　| 👁️　　👁️　|
// 　|　  👄　　　|
// 　ヽ＿＿ 　 　ノ
// 　 丿ﾉ ﾉ丁丁￣l＼
// 　く(_(_(＿L＿)ノ
//   イカだぜっ☆


// 　　　 fﾆヽ
// 　　　 |_||
// 　　　 |= |
// 　　　 |_ |
// 　　/⌒|~ |⌒i-、
// 　 /|　|　|　| ｜＼
// 　｜(　(　(　(　｜
// 　｜　　　　　 ｜
// 　 　　　　　/
// 　　 ＼　　　／
//  FXXK YOU

// ┏━┓
// ┃━┃
// ┃　┃
// ┃　┃━ ━ ━ ┓
// ┃　┃   ┃   ┃  ┃━\
// ┃　┃   ┃   ┃  ┃    /
// ┃　　　　　    ┃  /
// ┃　　　　　    ┃/
//  ＼━ ━ ━━  ┛

//         ？
// 　　　／￣￣￣＼
// 　　／ミ彡三ミ　＼
// 　 /ヽ　／⌒　　　ヽ
// 　(👁️)　👁️))　　 |
// 　|ー/　 ー　　　　|
// 　| (＿)_)　　　 ⌒)
// 　|/――＼ ヽ　 6ﾉ/∬
// 　ヽ￣￣＼ヽ|　 ノ
// 　 |ﾚｪｪｪ／ ||　/
// 　 |ー―′ ノ /
// 　 ヽ＿＿／　 ＼
// 　　　／　 ヽ| ｜
// 　　 /　　　|| ﾉ|
// 　　 ＼ ＼ ノ|｜|
// 　　　|ヽ )


// 　　　::::::::::::::::::::
// 　　　　::::::::::::::::
// 　　　　　::::::::::::
// 　　　Λ_Λ　:::::::
// 　　/彡ミﾍ )ー､ ::::
// 　 /:ﾉ:　ヽ ＼::|　:::
// 　/:｜::　 ＼ ヽ|　:::
// ￣L_ﾉ￣￣￣＼ノ￣￣

// 　　　　　　　／￣￣￣￣￣￣￣￣＼
// 　　　　　　/;;::　　　🩹　　　::;ヽ
// 　　　　　　|;;:: ｨ👁️ｧ　　ｨ👁️ｧ  ::;;|
// 　　　　　　|;;::　　　　　　　　::;;|
// 　　　　　　|;;:: 　　c{　っ　　::;;|
// 　　　　　　 |;;::　　＿＿　　::;;;|
// 　　　　　　 ヽ;;::　　ー　　::;;／
// 　　　　　　　　＼;;::　　::;;／
// 　　　　　　　　　 |;;::　 ::;;|
// 　　　　　　　　　 |;;::　 ::;;|
// 　　　／￣￣￣　　　　              ￣￣￣＼
// 　　　|;;::　　　　　　　　　　　　　　::;;|
// 　　　|;;::　　　　　　　　　　　　　　::;;