"use client";
import { BottomNavigation, BottomNavigationAction } from "@mui/material";
import HomeIcon from "@mui/icons-material/Home";
import StorefrontIcon from "@mui/icons-material/Storefront";
import SettingsIcon from "@mui/icons-material/Settings";
import InsightsIcon from "@mui/icons-material/Insights";
import LocalShippingIcon from "@mui/icons-material/LocalShipping";
import WarehouseIcon from "@mui/icons-material/Warehouse";
import LogoutIcon from "@mui/icons-material/Logout";
import { useRouter } from "next/navigation";

export default function NavigationMenu() {
  const router = useRouter();
  // const role = JSON.parse(sessionStorage.getItem("staff") ?? "").role;

  const handleNavigation = (path?: string) => {
    router.push(`/${path ?? ""}`);
  };

  const gtfo = () => {
    sessionStorage.removeItem("staff");
    router.push(`/`);
  };

  // TODO: Role based authorization to show/hide menu items, role is currently stored in sessionStorage

  return (
    <div className="fixed bottom-0 w-full justify-center flex">
      <BottomNavigation showLabels>
        {/* TODO: set active icon */}
        <BottomNavigationAction
          label="Dashboard"
          icon={<HomeIcon />}
          onClick={() => handleNavigation()}
        />
        {/* TODO:  {role === "Front-of-house" && ( */}
        <BottomNavigationAction
          label="POS"
          icon={<StorefrontIcon />}
          onClick={() => handleNavigation("pos")}
        />
        {/* )} */}
        <BottomNavigationAction
          label="Deliveries"
          icon={<LocalShippingIcon />}
          onClick={() => handleNavigation("deliveries")}
        />
        <BottomNavigationAction
          label="Inventory"
          icon={<WarehouseIcon />}
          onClick={() => handleNavigation("inventory")}
        />
        {/* TODO:  {role === "Manager" && ( */}
        <BottomNavigationAction
          label="Reports"
          icon={<InsightsIcon />}
          onClick={() => handleNavigation("reports")}
        />
        {/* )} */}
        <BottomNavigationAction
          label="Settings"
          icon={<SettingsIcon />}
          onClick={() => handleNavigation("settings")}
        />
        <BottomNavigationAction
          label="Log out"
          icon={<LogoutIcon />}
          onClick={gtfo}
        />
      </BottomNavigation>
    </div>
  );
}
