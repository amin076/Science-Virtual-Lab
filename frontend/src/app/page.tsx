import Link from "next/link";
import { Container, Typography, Box, Button, Paper } from "@mui/material";

export default function Home() {
  return (
    <Container maxWidth="sm" sx={{ py: 8 }}>
      <Paper sx={{ p: 4, borderRadius: 3, textAlign: "center", boxShadow: 3 }}>
        <Typography variant="h3" gutterBottom>
          🧪 Science Virtual Lab
        </Typography>
        <Typography variant="body1" color="text.secondary" sx={{ mb: 4 }}>
          Explore interactive science experiments powered by real physics
          simulations.
        </Typography>
        <Box>
          <Link href="/lab/pendulum" passHref>
            <Button variant="contained" size="large">
              Go to Pendulum Simulation
            </Button>
          </Link>
        </Box>
      </Paper>
    </Container>
  );
}
