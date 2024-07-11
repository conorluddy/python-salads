import type { Metadata } from "next";
import { Space_Grotesk as PrimaryTypeface } from "next/font/google";
import "./globals.css";
import Providers from "./providers";

const typeface = PrimaryTypeface({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Weird Salads!",
  description: "Technical challenge for Nory",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={typeface.className}>
        <Providers>{children}</Providers>
      </body>
    </html>
  );
}
