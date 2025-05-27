import { useEffect, useState } from "react";
import Layout from "../components/Layout";
import EmailSettingsForm from "../components/EmailSettingsForm";
import { fetchEmailSettings, updateEmailSettings } from "../utils/api";
import ProtectedRoute from "../components/ProtectedRoute";

export default function Settings() {
  const [settings, setSettings] = useState<any>(null);
  useEffect(() => { fetchEmailSettings().then(setSettings); }, []);
  return (
    <ProtectedRoute>
      <Layout>
        <h2>Settings</h2>
        {settings && <EmailSettingsForm settings={settings} onSave={updateEmailSettings} />}
      </Layout>
    </ProtectedRoute>
  );
}