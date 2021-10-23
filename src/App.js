import {  useState } from 'react';
import './App.css';

import LiveText from './components/LiveText';
import DifficultyBarChart from './components/DifficultyBarChart';
import dummy from './data/dummy.json';

function App() {

  const [speechText, setSpeechText] = useState('hi');

  return (
    <div className="App">
      <div className="layout">
        <LiveText width={70} text={speechText} setText={setSpeechText}/>
        <DifficultyBarChart data={dummy}/>
      </div>
    </div>
  );
}

export default App;
