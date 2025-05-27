import { useState } from "react";
import { useRouter } from "next/router";
import { TextField, Button, Typography } from "@mui/material";
import Layout from "../components/Layout";

export default function Signup() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [fullName, setFullName] = useState("");
  const router = useRouter();

  const handleSubmit = async (e: any) => {
    e.preventDefault();
    const res = await fetch("http://localhost:8000/users/signup", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, password, full_name: fullName }),
    });
    if (res.ok) {
      router.push("/login");
    } else {
      alert("Signup failed");
    }
  };

  return (
    <Layout>
      <Typography variant="h4" gutterBottom>Sign Up</Typography>
      <form onSubmit={handleSubmit}>
        <TextField label="Full Name" value={fullName} onChange={e => setFullName(e.target.value)} fullWidth margin="normal" />
        <TextField label="Email" value={email} onChange={e => setEmail(e.target.value)} fullWidth margin="normal" />
        <TextField label="Password" type="password" value={password} onChange={e => setPassword(e.target.value)} fullWidth margin="normal" />
        <Button type="submit" variant="contained" color="primary">Sign Up</Button>
      </form>
    </Layout>
  );
}