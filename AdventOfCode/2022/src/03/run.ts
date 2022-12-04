import * as library from "../library";

const asciiLowercase = "abcdefghijklmnopqrstuvwxyz";
const asciiUppercase = asciiLowercase.toUpperCase();
const asciiLowercaseUppercase = asciiLowercase + asciiUppercase;

function assert(condition: boolean, message: string) {
    if (!condition) {
        throw new Error(message);
    }
}

function getPriority(s: string) {
    assert(s.length === 1, `${s} has more than one character`);

    const index = asciiLowercaseUppercase.indexOf(s);
    assert(index !== -1, `${s} not found`);

    return index + 1;
}

function getSet(s: string) {
    return Array.from(s);
}

export function run(data: string) {
    // code
    const lines = library.getLines(data);

    // part 1
    const values = lines.map((line) => {
        // split into 2
        const pivot = line.length / 2;
        const compartmentA = line.slice(0, pivot);
        const compartmentB = line.slice(pivot);
        assert(
            compartmentA.length === compartmentB.length,
            `length ${compartmentA} != ${compartmentB}`
        );

        // intersection
        const a = getSet(compartmentA);
        const b = getSet(compartmentB);

        // intersection
        const same = a.filter((e) => b.includes(e));

        // keep only 1st element
        const uniqueSame = same.filter(
            (value, index, array) => array.findIndex((x) => x === value) === index
        );

        if (uniqueSame.length !== 1) {
            throw new Error(`expected one match for [${line}] = [${uniqueSame}]`);
        }

        const pick = uniqueSame[0];
        const priority = getPriority(pick);
        return priority;
    });
    const total = library.arraySum(values);
    console.log(total);

    // part 2

    // group into sets of 3 lines
    assert(lines.length % 3 === 0, "uneven groups");
    const groups = library.arrayGroup(lines, 3);
    //console.log(groups);

    const values2 = groups.map((group) => {
        const [a, b, c] = group.map((v) => getSet(v));

        // intersect all three lines
        const same = library.arrayUnique(
            library.arrayIntersection(library.arrayIntersection(a, b), c)
        );
        assert(same.length === 1, `need 1 same ${group}`);

        // get item type
        const pick = same[0];
        //console.log(pick);
        const priority = getPriority(pick);
        return priority;
    });
    const total2 = library.arraySum(values2);
    console.log(total2);
}
