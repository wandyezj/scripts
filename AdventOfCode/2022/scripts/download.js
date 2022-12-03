
async function downloadData(year, day, session) {
    const url = `https://adventofcode.com/${year}/day/${day}/input`;
    console.log(url)

    const response = await fetch(url, {
        headers: {
            Cookie: `session=${session}`
        }
    });

    const data = response.text();
    return data;
}


import process from 'process'
import fs from 'fs';

async function run() {
    const parameters = process.argv.slice(2)
    const [name, year, day, session] = parameters;

    if (year === "" || day === "" || session==="") {
        console.log("usage: year day session");
        return;
    }

    console.log(`
    year: ${year}
    day: ${day}
    session: ${session}
    `);

    const dayN = Number.parseInt(day).toString()
    const data = downloadData(year, dayN, session);

    const fileName = `${dayN.padStart(2, '0')}.data.txt`;

    console.log(fileName);
    fs.writeFileSync(fileName, data);
}

run();