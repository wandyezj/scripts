async function downloadData(year: number, day: number, session: string): Promise<string> {
    const url = `https://adventofcode.com/${year}/day/${day}/input`;
    console.log(url);

    const response = await fetch(url, {
        headers: {
            cookie: `session=${session}`,
        },
    });

    const data = response.text();
    return data;
}

// import process from "process";
import fs from "fs";

import { year, day, session } from "../session.json";

async function run() {
    // const parameters = process.argv.slice(2)
    // const [name, year, day, session] = parameters;

    if (year === undefined || day === undefined || session === "") {
        console.log("usage: year day session");
        return;
    }

    console.log(`
    year: ${year}
    day: ${day}
    session: ${session}
    `);

    // const dayN = Number.parseInt(day).toString();
    const data = await downloadData(year, day, session);

    const fileName = `${day.toString().padStart(2, "0")}.data.txt`;

    console.log(fileName);
    fs.writeFileSync(fileName, data);
}

run();
