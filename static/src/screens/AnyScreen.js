import React, { useContext } from 'react';
import FontContext from './FontContext';

const AnyScreen = () => {
  const { font } = useContext(FontContext);

  const screenStyle = {
    fontFamily: font, // フォントをスタイルに適用
  };

  return (
    <div style={screenStyle}>
    </div>
  );
};

export default AnyScreen;