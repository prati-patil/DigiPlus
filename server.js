const express = require('express');
const { simulateNetwork } = require('./simulation/network');
const app = express();

const PORT = 3000;

// API endpoint to trigger simulation
app.get('/simulate', (req, res) => {
    const result = simulateNetwork();
    res.send(result);
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
