import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route, useLocation } from 'react-router-dom';
import { TransitionGroup, CSSTransition } from 'react-transition-group';
import WelcomeScreen from './screens/WelcomeScreen';
import LoginScreen from './screens/LoginScreen';
import RegisterScreen from './screens/RegisterScreen';
import FriendsListScreen from './screens/FriendsListScreen';
import ChatScreen from './screens/ChatScreen';
import ChatListScreen from './screens/ChatListScreen';
import ProfileScreen from './screens/ProfileScreen';
import Navbar from './components/Navbar';
import FriendsAddScreen from './screens/FriendsAddScreen';
import SettingScreen from './screens/SettingScreen';
import './App.css'; 
import FontContext from './screens/FontContext';



// ルート遷移のアニメーションを処理するコンポーネント
const AnimatedSwitch = () => {
  const location = useLocation();

  return (
    <TransitionGroup>
      <CSSTransition
        key={location.key}
        classNames="fade"
        timeout={300}
      >
        <Routes location={location}>
          <Route path="/" element={<WelcomeScreen />} />
          <Route path="/login" element={<LoginScreen />} />
          <Route path="/register" element={<RegisterScreen />} />
          <Route path="/friends" element={<FriendsListScreen />} />
          <Route path="/talks" element={<ChatScreen />} />
          <Route path="/talkslist" element={<ChatListScreen />} />
          <Route path="/profile" element={<ProfileScreen />} />
          <Route path="/FriendsAdd" element={<FriendsAddScreen />} />
          <Route path="/Setting" element={<SettingScreen />} />
          
        </Routes>
      </CSSTransition>
    </TransitionGroup>
  );
};

// Navbarを含めるかどうかを決定するコンポーネント
const Layout = ({ noNavbarPaths }) => {
  const location = useLocation();
  const showNavbar = !noNavbarPaths.includes(location.pathname);

  return (
    <>
      {showNavbar && <Navbar />}
    </>
  );
};

const App = () => {
  const [font, setFont] = useState('ゴシック'); // フォント状態を追加
  const noNavbarPaths = ['/', '/login', '/register', '/talks']; // Navbarを表示しないパス
  
  return (
    // FontContext.Providerでアプリケーション全体をラップする
    <FontContext.Provider value={{ font, setFont }}>
      <div>
        <AnimatedSwitch />
        <Layout noNavbarPaths={noNavbarPaths} />
      </div>
    </FontContext.Provider>
  );
};

const AppWrapper = () => {
  const [font, setFont] = useState('ゴシック'); // フォントの状態

  return (
    <Router>
      <FontContext.Provider value={{ font, setFont }}>
        <App />
      </FontContext.Provider>
    </Router>
  );
};


export default AppWrapper;