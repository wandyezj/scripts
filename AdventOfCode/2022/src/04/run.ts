import * as library from "../library";

function parsePairs(data: string) {
    const lines = library.getLines(data);

    const pairs = lines.map((line) =>
        line.split(",").map((x) => x.split("-").map((n) => Number.parseInt(n)))
    );

    return pairs as [[number, number], [number, number]][];
}

/**
 * a within b
 * @param aStart
 * @param aEnd
 * @param bStart
 * @param bEnd
 */
function fullyContained(aStart: number, aEnd: number, bStart: number, bEnd: number) {
    // start of a is withing b start and be end
    return aStart >= bStart && aEnd <= bEnd;
}

function anyOverlap(aStart: number, aEnd: number, bStart: number, bEnd: number) {
    return (aStart >= bStart && aStart <= bEnd) || (aEnd >= bStart && aEnd <= bEnd);
}

export function part1(data: string) {
    // code
    const pairs = parsePairs(data);
    //console.log(pairs);

    // how many pairs fully contain the other?

    const allContained = pairs.filter(([[startA, endA], [startB, endB]]) => {
        // is is fully contained?
        return (
            fullyContained(startA, endA, startB, endB) || fullyContained(startB, endB, startA, endA)
        );
    });
    console.log(allContained.length);
}

export function part2(data: string) {
    // code
    const pairs = parsePairs(data);

    const allOverlap = pairs.filter(([[startA, endA], [startB, endB]]) => {
        return anyOverlap(startA, endA, startB, endB) || anyOverlap(startB, endB, startA, endA);
    });
    console.log(allOverlap.length);
}

export function run(data: string) {
    // code
    part1(data);
    part2(data);
}
