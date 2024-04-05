"use client";
import NavigationMenu from "@/components/ui/navigation-menu";
import useRequireAuth from "@/hooks/useAuth";

export default function Deliveries() {
  useRequireAuth();
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      Deliveries
      <small>
        Incoming deliveries would be managed in here, posting stock updates to
        our delivery tables and tracking which member of staff accepted the
        delivery
      </small>
      <NavigationMenu />
    </main>
  );
}
