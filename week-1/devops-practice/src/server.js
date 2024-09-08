// Server is responsible for starting the server and listening on a port.
const app = require('./app');

const server = app.listen(process.env.PORT || 3001, () => {
    console.log(`Server is running on port ${server.address().port}`);
});

module.exports = server;
