// App contains the Express application setup and routes.

// Importing express library
const express = require('express');

// Creating Express application
const app = express();

// GET request to root URL with basic response
app.get('/', (req, res) => {
    res.send('<h1>Hello World! 😉</h1>');
});

app.get('/multiply/:num1/:num2', (req, res) => {
    const { num1, num2 } = req.params;
    const product = num1 * num2;
    res.send(`<h1>${num1} * ${num2} = ${product}</h1>`);
});

// Exporting the app to be used in other files
module.exports = app;