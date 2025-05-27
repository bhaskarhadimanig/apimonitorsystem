import { useState } from "react";
import { TextField, Button } from "@mui/material";

export default function ApiForm({ api, onSave }) {
  const [form, setForm] = useState(api || { name: "", url: "", frequency: 60 });
  return (
    <form onSubmit={e => { e.preventDefault(); onSave(form); }}>
      <TextField label="Name" value={form.name} onChange={e => setForm({ ...form, name: e.target.value })} fullWidth />
      <TextField label="URL" value={form.url} onChange={e => setForm({ ...form, url: e.target.value })} fullWidth />
      <TextField label="Frequency (sec)" type="number" value={form.frequency} onChange={e => setForm({ ...form, frequency: +e.target.value })} fullWidth />
      <Button type="submit" variant="contained" color="primary">Save</Button>
    </form>
  );
}