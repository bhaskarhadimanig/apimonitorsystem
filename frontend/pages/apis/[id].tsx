import { useRouter } from "next/router";
import { useEffect, useState } from "react";
import ApiForm from "../../components/ApiForm";
import { fetchApi, updateApi } from "../../utils/api";
import Layout from "../../components/Layout";
import ProtectedRoute from "../../components/ProtectedRoute";

export default function ApiDetail() {
  const router = useRouter();
  const { id } = router.query;
  const [api, setApi] = useState<any>(null);

  useEffect(() => {
    if (id) fetchApi(id as string).then(setApi);
  }, [id]);

  return (
    <ProtectedRoute>
      <Layout>
        <h2>Edit API</h2>
        {api && <ApiForm api={api} onSave={data => updateApi(id as string, data)} />}
      </Layout>
    </ProtectedRoute>
  );
}