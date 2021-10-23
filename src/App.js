import { useEffect, useState } from 'react';
import './App.css';

import LiveText from './components/LiveText';

function App() {

  const [speechText, setSpeechText] = useState('hi');

  return (
    <div className="App">
      <header className="App-header">
        <LiveText text={speechText}/>
      </header>
    </div>
  );
}

export default App;
