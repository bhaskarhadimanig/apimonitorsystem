import Layout from "../components/Layout";
import { Button } from "@mui/material";
import Link from "next/link";

export default function Home() {
  return (
    <Layout>
      <section style={{ textAlign: "center", marginTop: 80 }}>
        <h1>API Availability Monitoring SaaS</h1>
        <p>Reliable API uptime monitoring for your business. Role-based access, real-time alerts, beautiful charts.</p>
        <Link href="/signup"><Button variant="contained" color="primary" size="large">Get Started</Button></Link>
      </section>
    </Layout>
  );
}