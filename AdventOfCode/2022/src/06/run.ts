import * as library from "../library";

function parseData(data: string) {
    const line = library.getLines(data)[0];
    return line;
}

export function part1(data: string) {
    // code
    const stream = parseData(data);

    let i = 3;
    for (; i < stream.length; i++) {
        const chunk = stream.substring(i - 4, i);

        // is unique

        if (library.arrayUnique(Array.from(chunk)).length === 4) {
            break;
        }
    }

    console.log(i);
}

export function part2(data: string) {
    // code
    const stream = parseData(data);

    const n = 14;
    let i = n - 1;
    for (; i < stream.length; i++) {
        const chunk = stream.substring(i - n, i);

        // is unique

        if (library.arrayUnique(Array.from(chunk)).length === n) {
            break;
        }
    }

    console.log(i);
}

export function run(data: string) {
    // code
    part1(data);
    part2(data);
}
