import { day } from "../session.json";

const dayDirectory = day.toString().padStart(2, "0");

const script = require(`../src/${dayDirectory}/run.ts`);

import fs from "fs";

const data = fs.readFileSync(`src/${dayDirectory}/data.sample.txt`, "utf-8");

script.run(data);
