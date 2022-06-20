import { hello } from "../src/index";
//import 'expect-puppeteer';
import * as puppeteer from "puppeteer";
import { startServer } from "./startServer";
import { serverPort } from "./constants";
import { Server } from "http";

test("basic", () => {
    const actual = hello();
    const expected = "hello";
    expect(actual).toBe(expected);
});

describe("test-page", () => {
    let page: puppeteer.Page;
    let server: Server;
    beforeAll(async () => {
        server = startServer(serverPort);
        const browser = await puppeteer.launch({ headless: false });
        page = await browser.newPage();
        await page.goto(`http://localhost:${serverPort}/test-page.html`);
    });

    afterAll(async () => {
        await Promise.all(
            [
                new Promise((resolve) => server.close(resolve)),
                page.close()
            ]);

    });

    test("page basic", async () => {
        const expected = "hello";
        const result = await page.evaluate(`(async() => {
            return "hi"
            //let result = testHello();
            //return result;
        })()`);

        expect(result).toBe(expected);
    });
});


