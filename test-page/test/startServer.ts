import http from "http";
import path from "path";
import * as fs from "fs";

// all valid resources
const serveResources = [
    "test-page.js",
    "test-page.html"
];

// don't bother with express just write a simple node server.
export function startServer(port: number) {
    const server = http.createServer((req, res) => {
        const {url} =  req;
        //console.log(req.url);

        const found = serveResources.filter((value) => `/${value}` === url );
        //console.log(found);

        if (found.length === 1) {
            const fileName = found[0];
            const filePath = path.join(__dirname + `/resources/${fileName}`);
            const fileData = fs.readFileSync(filePath)

            res.write(fileData);
        } else {
            res.write(`Not Found\n\nValid Resources:\n\n${serveResources.join("\n")}`);
        }

        res.end();
    });

    server.listen(port);

    return server;
}