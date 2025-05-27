import type { AppProps } from "next/app";
import { AuthProvider } from "../context/AuthContext";
import CssBaseline from "@mui/material/CssBaseline";

export default function App({ Component, pageProps }: AppProps) {
  return (
    <AuthProvider>
      <CssBaseline />
      <Component {...pageProps} />
    </AuthProvider>
  );
}