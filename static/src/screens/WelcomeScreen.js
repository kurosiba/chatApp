import React, { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import welcomeGif from '../assets/images/gear.gif';

const WelcomeScreen = () => {
  const navigate = useNavigate();

  useEffect(() => {
    const timer = setTimeout(() => {
      navigate('/login');
    }, 1000);

    return () => clearTimeout(timer);
  }, [navigate]);

  return (
    // Flexboxを使用して中央揃え
    <div style={{
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      justifyContent: 'center',
      height: '100vh', // 画面の高さに合わせる
    }}>
      <p>Welcome to our app!</p>
      <img src={welcomeGif} alt="Welcome" style={{ width: '50%', height: 'auto' }} />
    </div>
  );
};

export default WelcomeScreen;