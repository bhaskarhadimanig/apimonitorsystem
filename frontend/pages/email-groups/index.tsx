import { useEffect, useState } from "react";
import Layout from "../../components/Layout";
import EmailGroupTable from "../../components/EmailGroupTable";
import { fetchEmailGroups } from "../../utils/api";
import ProtectedRoute from "../../components/ProtectedRoute";

export default function EmailGroups() {
  const [groups, setGroups] = useState<any[]>([]);
  useEffect(() => { fetchEmailGroups().then(setGroups); }, []);
  return (
    <ProtectedRoute>
      <Layout>
        <h2>Email Groups</h2>
        <EmailGroupTable groups={groups} />
      </Layout>
    </ProtectedRoute>
  );
}