"use client";

import React, { useState } from "react";
import {
  Container,
  Typography,
  TextField,
  Button,
  Box,
  Paper,
  CircularProgress,
} from "@mui/material";
import {
  LineChart,
  Line,
  CartesianGrid,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

export default function PendulumLabPage() {
  const [form, setForm] = useState({
    theta0_deg: 10,
    length_m: 1.0,
    g: 9.81,
    t: 1.0,
  });
  const [result, setResult] = useState<any>(null);
  const [chartData, setChartData] = useState<any[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setForm({ ...form, [e.target.name]: parseFloat(e.target.value) });
  };

  const runSimulation = async () => {
    setLoading(true);
    setError(null);
    try {
      const res = await fetch("http://127.0.0.1:8000/sim/pendulum", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(form),
      });
      if (!res.ok) throw new Error(`Server error: ${res.status}`);
      const data = await res.json();
      setResult(data);

      // Generate sample angle values over time (for visualization)
      const omega = data.omega;
      const theta0 = (form.theta0_deg * Math.PI) / 180;
      const points = [];
      for (let i = 0; i <= 100; i++) {
        const t = (i / 100) * 10; // 0 → 10 seconds
        const theta_t = theta0 * Math.cos(omega * t);
        points.push({
          time: t.toFixed(2),
          theta_deg: (theta_t * 180) / Math.PI,
        });
      }
      setChartData(points);
    } catch (err: any) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <Container maxWidth="md" sx={{ py: 4 }}>
      <Paper sx={{ p: 4, borderRadius: 3, boxShadow: 3 }}>
        <Typography variant="h4" gutterBottom>
          Pendulum Simulation
        </Typography>

        <Typography variant="body2" color="text.secondary" sx={{ mb: 2 }}>
          Adjust the parameters below and run the simulation to see the motion.
        </Typography>

        <Box sx={{ display: "grid", gap: 2, mb: 2 }}>
          <TextField
            label="Initial Angle (degrees)"
            name="theta0_deg"
            type="number"
            value={form.theta0_deg}
            onChange={handleChange}
          />
          <TextField
            label="Length (meters)"
            name="length_m"
            type="number"
            value={form.length_m}
            onChange={handleChange}
          />
          <TextField
            label="Gravity (m/s²)"
            name="g"
            type="number"
            value={form.g}
            onChange={handleChange}
          />
          <TextField
            label="Time (seconds)"
            name="t"
            type="number"
            value={form.t}
            onChange={handleChange}
          />
          <Button
            variant="contained"
            onClick={runSimulation}
            disabled={loading}
            sx={{ mt: 1 }}
          >
            {loading ? <CircularProgress size={24} /> : "Run Simulation"}
          </Button>
        </Box>

        {error && (
          <Typography color="error" sx={{ mt: 2 }}>
            {error}
          </Typography>
        )}

        {result && (
          <Box sx={{ mt: 4 }}>
            <Typography variant="h6" gutterBottom>
              Simulation Results:
            </Typography>
            <Typography>
              θ (radians): <strong>{result.theta_rad.toFixed(4)}</strong>
            </Typography>
            <Typography>
              θ (degrees): <strong>{result.theta_deg.toFixed(2)}</strong>
            </Typography>
            <Typography>
              ω (rad/s): <strong>{result.omega.toFixed(2)}</strong>
            </Typography>
          </Box>
        )}

        {chartData.length > 0 && (
          <Box sx={{ mt: 5 }}>
            <Typography variant="h6" gutterBottom>
              Pendulum Angle Over Time
            </Typography>
            <ResponsiveContainer width="100%" height={300}>
              <LineChart data={chartData}>
                <CartesianGrid stroke="#ccc" strokeDasharray="5 5" />
                <XAxis
                  dataKey="time"
                  label={{
                    value: "Time (s)",
                    position: "insideBottom",
                    offset: -5,
                  }}
                />
                <YAxis
                  label={{
                    value: "Angle (°)",
                    angle: -90,
                    position: "insideLeft",
                  }}
                />
                <Tooltip />
                <Line
                  type="monotone"
                  dataKey="theta_deg"
                  stroke="#1976d2"
                  strokeWidth={2}
                  dot={false}
                />
              </LineChart>
            </ResponsiveContainer>
          </Box>
        )}
      </Paper>
    </Container>
  );
}
