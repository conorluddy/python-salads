"use client";

import React, { useState } from "react";
import { useRouter } from "next/navigation";
import { TextField, Button, Typography, Container } from "@mui/material";
import { API_BASE_URL } from "@/constants";
import { redirect } from "next/navigation";

const Login = () => {
  const router = useRouter();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleSubmit = async (e) => {
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
        router.push("/dashboard");
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
          <Typography variant="h4" gutterBottom>
            Login
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
            <Button type="submit" variant="contained" color="primary" fullWidth>
              Login
            </Button>
          </form>
        </div>
      </Container>
    </main>
  );
};

export default Login;
