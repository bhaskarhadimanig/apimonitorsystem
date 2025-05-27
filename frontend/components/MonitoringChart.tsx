import { Line } from "react-chartjs-2";
import { Chart, LineElement, CategoryScale, LinearScale, PointElement } from "chart.js";
Chart.register(LineElement, CategoryScale, LinearScale, PointElement);

export default function MonitoringChart({ data }) {
  const chartData = {
    labels: data.map((x: any, i: number) => x.api_id || i),
    datasets: [
      {
        label: 'API Avg Response Time (ms)',
        data: data.map((x: any) => x.avg),
        fill: false,
        borderColor: 'rgb(75,192,192)',
        tension: 0.1,
      },
    ],
  };
  return (
    <Line data={chartData} />
  );
}