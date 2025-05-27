import { useAuth } from "../context/AuthContext";
import { useRouter } from "next/router";
import { useEffect } from "react";

export default function ProtectedRoute({ children }) {
  const { user } = useAuth();
  const router = useRouter();
  useEffect(() => {
    if (!user) router.push("/login");
  }, [user, router]);
  return user ? children : null;
}