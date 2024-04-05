import { Typography } from "@mui/material";
import Image from "next/image";

const BASE_URL = "http://127.0.0.1:8000";

export default async function Home() {
  const data = await getData();

  return (
    <main className="flex flex-col items-center justify-between p-24 gap-10">
      <Image src="/shnake.svg" width={200} height={200} alt="Weird Salads" />
      <Typography variant="h2">Weird Salads</Typography>

      <pre>{JSON.stringify(data, null, 2)}</pre>
    </main>
  );
}

async function getData() {
  const res = await fetch(`${BASE_URL}/locations`);

  if (!res.ok) {
    // This will activate the closest `error.js` Error Boundary
    throw new Error("Failed to fetch data");
  }

  return res.json();
}
