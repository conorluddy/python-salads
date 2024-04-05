"use client";

import { Typography } from "@mui/material";
import Image from "next/image";
import useRequireAuth from "@/hooks/useAuth";
import NavigationMenu from "@/components/ui/navigation-menu";

export default function Dashboard() {
  useRequireAuth();

  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <div className="flex flex-col items-center justify-between gap-10">
        <Image src="/shnake.svg" width={100} height={100} alt="Weird Salads" />
        <Typography variant="h4" className="uppercase">
          Weird Salads
        </Typography>
      </div>

      <NavigationMenu />
    </main>
  );
}
