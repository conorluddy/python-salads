"use client";
import NavigationMenu from "@/components/ui/navigation-menu";
import RecipeList from "@/components/ui/recipe-list";
import useRequireAuth from "@/hooks/useAuth";

export default function PointOfSales() {
  useRequireAuth();
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      Point of Sales
      <RecipeList />
      <NavigationMenu />
    </main>
  );
}
