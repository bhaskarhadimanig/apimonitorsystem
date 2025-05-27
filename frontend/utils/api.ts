const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

function getToken() {
  return typeof window !== "undefined" ? localStorage.getItem("token") : null;
}

export async function fetchUserApis() {
  const res = await fetch(`${API_URL}/apis`, {
    headers: { 'Authorization': `Bearer ${getToken()}` }
  });
  return res.json();
}

export async function fetchApiStats() {
  const res = await fetch(`${API_URL}/monitor/stats`, {
    headers: { 'Authorization': `Bearer ${getToken()}` }
  });
  return res.json();
}

export async function fetchApi(id: string) {
  const res = await fetch(`${API_URL}/apis/${id}`, {
    headers: { 'Authorization': `Bearer ${getToken()}` }
  });
  return res.json();
}

export async function updateApi(id: string, data: any) {
  const res = await fetch(`${API_URL}/apis/${id}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json", 'Authorization': `Bearer ${getToken()}` },
    body: JSON.stringify(data)
  });
  return res.json();
}

export async function fetchEmailGroups() {
  const res = await fetch(`${API_URL}/email-groups`, {
    headers: { 'Authorization': `Bearer ${getToken()}` }
  });
  return res.json();
}

export async function fetchEmailSettings() {
  const res = await fetch(`${API_URL}/settings/email`, {
    headers: { 'Authorization': `Bearer ${getToken()}` }
  });
  return res.json();
}

export async function updateEmailSettings(data: any) {
  const res = await fetch(`${API_URL}/settings/email`, {
    method: "PUT",
    headers: { "Content-Type": "application/json", 'Authorization': `Bearer ${getToken()}` },
    body: JSON.stringify(data)
  });
  return res.json();
}