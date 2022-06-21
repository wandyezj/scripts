import { hello } from "../src/index";
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
    let browser: puppeteer.Browser;
    let page: puppeteer.Page;
    let server: Server;
    beforeAll(async () => {
        server = startServer(serverPort);
        browser = await puppeteer.launch({ headless: true });
        page = await browser.newPage();
        await page.goto(`http://localhost:${serverPort}/test-page.html`);
    });

    afterAll(async () => {
        server.close();
        await page.close();
        await browser.close();
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
