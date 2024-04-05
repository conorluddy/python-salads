"use client";

import React, { ChangeEvent, useState } from "react";
import { useRouter } from "next/navigation";
import { TextField, Button, Typography, Container } from "@mui/material";
import Image from "next/image";
import { API_BASE_URL } from "@/constants";

const Login = () => {
  const router = useRouter();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleSubmit = async (e: { preventDefault: () => void; }) => {
    e.preventDefault();
    try {
      const response = await fetch(`${API_BASE_URL}/auth/login`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ email, password }),
      });
      if (response.ok) {
        const staff = await response.json(); // Assuming the response body contains the staff data

        sessionStorage.setItem("staff", JSON.stringify(staff));
        router.push("/");
      } else {
        setError("Invalid email or password");
      }
    } catch (error) {
      console.error(error);
      setError("An error occurred while processing your request");
    }
  };

  return (
    <main className="flex flex-col items-center justify-between p-24 gap-10">
      <Container maxWidth="xs">
        <div>
          <div className="flex flex-col items-center justify-between gap-10 mb-10">
            <Image
              src="/shnake.svg"
              width={100}
              height={100}
              alt="Weird Salads"
            />
            <Typography variant="h4" className="uppercase">
              Weird Salads
            </Typography>

            <small>Hint: lorenzo.will@weirdsalads.com | 1111</small>
            <form onSubmit={handleSubmit}>
              <TextField
                label="Email"
                variant="outlined"
                fullWidth
                margin="normal"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
              />
              <TextField
                label="Password"
                type="password"
                variant="outlined"
                fullWidth
                margin="normal"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
              />
              {error && (
                <Typography variant="body2" color="error">
                  {error}
                </Typography>
              )}
              <Button
                type="submit"
                variant="contained"
                color="primary"
                fullWidth
                className="mt-10"
              >
                Login
              </Button>
            </form>
          </div>
        </div>
      </Container>
    </main>
  );
};

export default Login;
