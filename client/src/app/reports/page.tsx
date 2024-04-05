"use client";
import NavigationMenu from "@/components/ui/navigation-menu";
import useRequireAuth from "@/hooks/useAuth";

export default function Reports() {
  useRequireAuth();
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      Reporting
      <small>
        Reporting would probably need a few sub-routes to handle the various
        kinds of reports we may need. The Dashboard would be a nice place to
        show summaries of same, assuming the logged in staff member had
        permission to see same.
      </small>
      <NavigationMenu />
    </main>
  );
}
