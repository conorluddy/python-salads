"use client";
import IngredientsList from "@/components/ui/inventory-list";
import NavigationMenu from "@/components/ui/navigation-menu";
import useRequireAuth from "@/hooks/useAuth";

export default function Inventory() {
  useRequireAuth();
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      Inventory
      <IngredientsList />
      <NavigationMenu />
    </main>
  );
}
