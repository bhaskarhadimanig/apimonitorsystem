import { useState } from "react";
import { TextField, Button } from "@mui/material";

export default function EmailSettingsForm({ settings, onSave }) {
  const [fromEmail, setFromEmail] = useState(settings.from_email || "");
  return (
    <form onSubmit={e => { e.preventDefault(); onSave({ from_email: fromEmail }); }}>
      <TextField label="From Email" value={fromEmail} onChange={e => setFromEmail(e.target.value)} fullWidth />
      <Button type="submit" variant="contained" color="primary">Save</Button>
    </form>
  );
}