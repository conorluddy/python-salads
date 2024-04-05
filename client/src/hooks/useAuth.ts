import { useRouter } from "next/navigation";
import { useEffect } from "react";

const useRequireAuth = () => {
  const router = useRouter();

  useEffect(() => {
    const userData = sessionStorage.getItem("staff");
    if (!userData) {
      router.push("/login");
    }
  }, []);

  return;
};

export default useRequireAuth;
