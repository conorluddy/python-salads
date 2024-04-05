"use client";
import useRequireAuth from "@/hooks/useAuth";

export default function Settings() {
  useRequireAuth();
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      Settings
    </main>
  );
}
