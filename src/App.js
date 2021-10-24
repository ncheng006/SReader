import { useEffect, useState } from "react";
import "./App.css";

import LiveText from "./components/LiveText";
import DifficultyBarChart from "./components/DifficultyBarChart";
import dummy_pace from "./data/dummy-pace.json";
import dummy_metrics from "./data/dummy-metrics.json";

function App() {
  const [speechLevel, setSpeechLevel] = useState(75);
  const [text, setText] = useState("hi");
  const [paceData, setPaceData] = useState(dummy_pace);
  const [metricsData, setMetricsData] = useState(dummy_metrics);

  useEffect(() => {
    fetch("/transcribe");

    const interval = setInterval(() => {
      fetch("/read")
        .then((res) => res.json())
        .then((data) => {
          setText(data.lines);
        });

      fetch("/paceData")
        .then((res) => res.json())
        .then((data) => {
          setPaceData(data.values);
        });

      fetch("/all_metrics")
        .then((res) => res.json())
        .then((data) => {
          setMetricsData(data.values);
        });

    }, 1000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="App">
      <div className="layout">
        <LiveText width={speechLevel} text={text} />
        <DifficultyBarChart
          paceData={paceData}
          metricsData={metricsData}
        />
      </div>
    </div>
  );
}

export default App;
