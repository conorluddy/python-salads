"use client";
import NavigationMenu from "@/components/ui/navigation-menu";
import RecipeList from "@/components/ui/recipe-list";
import useRequireAuth from "@/hooks/useAuth";

export default function PointOfSales() {
  useRequireAuth();
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      Point of Sales
      <small className="m-10">
        This page would ideally have actions where you can click the recipes to
        add them to the order, and let you manage the modifiers/allergens on
        each item. We&apos;re also missing our prices in the api data.
      </small>
      <RecipeList />
      <NavigationMenu />
    </main>
  );
}
