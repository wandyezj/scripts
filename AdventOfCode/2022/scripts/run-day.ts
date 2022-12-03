import { day } from "../session.json";

const dayDirectory = day.toString().padStart(2, "0");

const script = require(`../src/${dayDirectory}/run.ts`);

import fs from "fs";

const [inputFileName] = process.argv.slice(2);

const data = fs
    .readFileSync(`src/${dayDirectory}/${inputFileName}`, "utf-8")
    .replace(/\r\n/g, "\n");

script.run(data);
