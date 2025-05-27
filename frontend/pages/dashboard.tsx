import { useEffect, useState } from "react";
import Layout from "../components/Layout";
import ApiTable from "../components/ApiTable";
import MonitoringChart from "../components/MonitoringChart";
import { fetchUserApis, fetchApiStats } from "../utils/api";
import ProtectedRoute from "../components/ProtectedRoute";

export default function Dashboard() {
  const [apis, setApis] = useState([]);
  const [stats, setStats] = useState<any>({});

  useEffect(() => {
    fetchUserApis().then(setApis);
    fetchApiStats().then(setStats);
  }, []);

  return (
    <ProtectedRoute>
      <Layout>
        <h2>Your APIs</h2>
        <ApiTable apis={apis} />
        <h3>API Monitoring Stats</h3>
        <MonitoringChart data={stats.responseTimes || []} />
      </Layout>
    </ProtectedRoute>
  );
}