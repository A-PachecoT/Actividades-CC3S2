const request = require('supertest');
const app = require('../src/app');
// const server = require('../src/server');

describe('GET /', () => {

    // beforeAll(async () => {
    //     server.listen(0); // Start server before all tests
    //     // The port is automatically assigned by the operating system
    // });

    // afterAll(async () => {
    //     server.close(); // Close server after all tests
    // })

    it('should return Hello, World!', async () => {
        const res = await request(app).get('/');
        expect(res.statusCode).toEqual(200);
        // This checks the entire response text, including that it is an HTML response.
        expect(res.text).toEqual('<h1>Hello World! 😉</h1>');
    });

    it('should return the product of two numbers', async () => {
        const res = await request(app).get('/multiply/3/4');
        expect(res.statusCode).toEqual(200);
        expect(res.text).toEqual('<h1>3 * 4 = 12</h1>');
    });
});