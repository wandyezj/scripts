import * as library from "../library";

function parsePuzzle(data: string) {
    const lines = library.getLines(data);

    // collect stacks
    // collect moves
    // number, from, to

    const stacks: string[][] = [[], [], [], [], [], [], [], [], [], []]; // there are 9 max
    const moves: { move: number; from: number; to: number }[] = [];

    lines.forEach((line) => {
        if (["[", " "].includes(line[0])) {
            //console.log(line);
            let chunk = line;
            let index = 1;
            while (chunk.length > 0) {
                const piece = chunk.substring(0, 3);
                //console.log(piece);
                if (piece.startsWith("[") && piece.endsWith("]")) {
                    const character = piece[1];
                    stacks[index].push(character);
                }

                index++;
                chunk = chunk.substring(4);
            }
        } else if (line.startsWith("move")) {
            const regex = /move (?<move>[0-9]*) from (?<from>[0-9]*) to (?<to>[0-9]*)/;
            const results = regex.exec(line);
            const groups = results?.groups!;

            const getValue = (value: string) => Number.parseInt(groups[value]);

            const move = getValue("move");
            const from = getValue("from");
            const to = getValue("to");

            moves.push({ move, from, to });
        }
    });

    stacks.forEach((stack) => {
        stack.reverse();
    });

    return { stacks, moves };
}

function calcLetters(stacks: string[][]) {
    const letters = stacks
        .map((stack) => (stack.length > 0 ? stack[stack.length - 1] : ""))
        .join("");
    return letters;
}

export function part1(data: string) {
    // code
    const puzzle = parsePuzzle(data);
    //console.log(puzzle);
    const { moves, stacks } = puzzle;
    // run puzzle
    moves.forEach(({ move, from, to }) => {
        for (let i = 0; i < move; i++) {
            const box = stacks[from].pop()!;
            stacks[to].push(box);
        }
    });

    //console.log(stacks);

    const letters = calcLetters(stacks);
    console.log(letters);
}

export function part2(data: string) {
    // code
    const puzzle = parsePuzzle(data);
    const { moves, stacks } = puzzle;

    // run crane
    moves.forEach(({ move, from, to }) => {
        const boxes: string[] = [];
        for (let i = 0; i < move; i++) {
            const box = stacks[from].pop()!;
            boxes.push(box);
        }

        boxes.reverse();
        stacks[to].push(...boxes);
    });

    //console.log(stacks);

    const letters = calcLetters(stacks);
    console.log(letters);
}

export function run(data: string) {
    // code
    part1(data);
    part2(data);
}
