import { useEffect, useState } from "react";
import "./App.css";

import LiveText from "./components/LiveText";
import DifficultyBarChart from "./components/DifficultyBarChart";
import dummy from "./data/dummy.json";

function App() {
  const [text, setText] = useState("hi");
  const [data, setData] = useState(dummy);

  useEffect(() => {
    const interval = setInterval(() => {
      console.log("This will run every second!");

      fetch("/transcribe")
        .then((res) => res.json())
        .then((data) => {
          console.log(data.lines);
          setText(data.lines);
        });

      fetch("/data")
        .then((res) => res.json())
        .then((data) => {
          setData(data.values);
        });
    }, 1000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="App">
      <div className="layout">
        <LiveText width={20} text={text} />
        <DifficultyBarChart data={data} />
      </div>
    </div>
  );
}

export default App;
