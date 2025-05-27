import { Container, AppBar, Toolbar, Typography, Button } from "@mui/material";
import Link from "next/link";
import { useAuth } from "../context/AuthContext";

export default function Layout({ children }) {
  const { user, logout } = useAuth();
  return (
    <>
      <AppBar position="static">
        <Toolbar>
          <Link href="/" style={{ textDecoration: "none", color: "white" }}>
            <Typography variant="h6" style={{ flexGrow: 1 }}>API Monitor SaaS</Typography>
          </Link>
          {user ? (
            <>
              <Link href="/dashboard"><Button color="inherit">Dashboard</Button></Link>
              <Link href="/apis"><Button color="inherit">My APIs</Button></Link>
              <Link href="/email-groups"><Button color="inherit">Email Groups</Button></Link>
              <Link href="/settings"><Button color="inherit">Settings</Button></Link>
              <Button color="inherit" onClick={logout}>Logout</Button>
            </>
          ) : (
            <>
              <Link href="/login"><Button color="inherit">Login</Button></Link>
              <Link href="/signup"><Button color="inherit">Signup</Button></Link>
            </>
          )}
        </Toolbar>
      </AppBar>
      <Container style={{ marginTop: 24 }}>{children}</Container>
    </>
  );
}