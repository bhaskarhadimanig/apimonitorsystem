import { useEffect, useState } from "react";
import Layout from "../../components/Layout";
import ApiTable from "../../components/ApiTable";
import { fetchUserApis } from "../../utils/api";
import ProtectedRoute from "../../components/ProtectedRoute";

export default function Apis() {
  const [apis, setApis] = useState([]);
  useEffect(() => { fetchUserApis().then(setApis); }, []);
  return (
    <ProtectedRoute>
      <Layout>
        <h2>My APIs</h2>
        <ApiTable apis={apis} />
      </Layout>
    </ProtectedRoute>
  );
}