"use client";
import NavigationMenu from "@/components/ui/navigation-menu";
import useRequireAuth from "@/hooks/useAuth";

export default function Settings() {
  useRequireAuth();
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      Settings
      <small>A place for general settings for our application</small>
      <NavigationMenu />
    </main>
  );
}
