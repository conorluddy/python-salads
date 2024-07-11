import ProviderQueryClient from "./ProviderQueryClient";

export default function Providers({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return <ProviderQueryClient>{children}</ProviderQueryClient>;
}
