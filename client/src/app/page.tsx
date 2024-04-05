"use client";

import { Typography } from "@mui/material";
import Image from "next/image";
import useRequireAuth from "@/hooks/useAuth";
import NavigationMenu from "@/components/ui/navigation-menu";
import { useEffect, useState } from "react";

export default function Dashboard() {
  useRequireAuth();

  const [userName, setUserName] = useState<string>();

  // Using useEffect here as a hacky las minute workaround for the sessionStorage not being available in the server-side
  useEffect(() => {
    const userData = sessionStorage.getItem("staff");
    if (userData) setUserName(JSON.parse(userData).name);
  }, []);

  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <div className="flex flex-col items-center justify-between gap-10">
        <Image src="/shnake.svg" width={100} height={100} alt="Weird Salads" />
        <Typography variant="h4" className="uppercase">
          Weird Salads
        </Typography>

        <p>Hello {userName}!</p>
        <p>Welcome back to our half-built application!</p>
      </div>

      <NavigationMenu />
    </main>
  );
}
