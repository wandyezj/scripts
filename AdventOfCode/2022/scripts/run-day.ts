import { year, day, session } from "../session.json";
import fs from "fs";
import path from "path";

function padDay(day: number) {
    return day.toString().padStart(2, "0");
}

const dayDirectory = padDay(day);

function runDay(dayDirectory: string, inputFileName: string) {
    const script = require(`../src/${dayDirectory}/run.ts`);

    const data = fs
        .readFileSync(`src/${dayDirectory}/${inputFileName}`, "utf-8")
        .replace(/\r\n/g, "\n");

    script.run(data);
}

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

async function setupDay(dayDirectory: string) {
    const dayDirectoryPath = `src/${dayDirectory}`;

    // if the day directory exists bail out
    if (fs.existsSync(dayDirectoryPath)) {
        console.log(dayDirectoryPath);
        return;
    }

    // create directory
    fs.mkdirSync(dayDirectoryPath, { recursive: true });

    // create data.sample.txt
    const data = await downloadData(year, day, session);

    const nameData: [string, string][] = [
        ["data.txt", data],
        ["data.sample.txt", ""],
        ["puzzle.txt", ""],
        [
            "run.ts",
            `
export function run(data: string) {
    // code
}
`,
        ],
    ];

    nameData.forEach(([name, data]) => {
        const filePath = path.join(dayDirectoryPath, name);
        fs.writeFileSync(filePath, data);
    });
}

async function run() {
    const [command, inputFileName] = process.argv.slice(2);

    switch (command) {
        case "run":
            runDay(dayDirectory, inputFileName);
            break;
        case "setup":
            await setupDay(dayDirectory);
            break;
        default:
            console.log(`unknown command ${command}`);
    }
}

run();
