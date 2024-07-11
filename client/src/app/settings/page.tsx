import {
  dehydrate,
  HydrationBoundary,
  QueryClient,
} from "@tanstack/react-query";
import NavigationMenu from "@/components/ui/navigation-menu";

// import useRequireAuth from "@/hooks/useAuth";

export default async function Settings() {
  // useRequireAuth();
  const queryClient = new QueryClient();

  await queryClient.prefetchQuery({
    queryKey: ["locations"],
    // queryFn: getLocations,
  });

  return (
    // Neat! Serialization is now as easy as passing props.
    // HydrationBoundary is a Client Component, so hydration will happen there.
    <HydrationBoundary state={dehydrate(queryClient)}>
      <main className="flex min-h-screen flex-col items-center justify-between p-24">
        Settings
        <small>A place for general settings for our application</small>
        <NavigationMenu />
      </main>
    </HydrationBoundary>
  );
}
