"use client";
import NavigationMenu from "@/components/ui/navigation-menu";
import useRequireAuth from "@/hooks/useAuth";

export default function Dashboard() {
  useRequireAuth();

  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      Dashboard
      <NavigationMenu />
    </main>
  );
}
