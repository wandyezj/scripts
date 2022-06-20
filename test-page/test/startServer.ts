import http, { Server } from "http";
import express from "express";
import path from "path";

// starts server to serve specific resources
export function startServer(port: number): Server {
    //const port: number = serverPort;
    const app = express();
    
    const serveResources = [
        "test-page.js",
        "test-page.html"
    ];

    serveResources.forEach((file) => {
        app.get(`/${file}`, (_req, res) => {
            res.sendFile(path.join(__dirname + `/resources/${file}`));
        });
    });
    
    const server = http.createServer(app);
    server.listen(port);

    return server;
}
