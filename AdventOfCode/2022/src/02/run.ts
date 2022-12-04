import { arraySum } from "../library/arraySum";

export function run(data: string) {
    const lines = data.trimEnd().split("\n");

    // code
    // opponent

    // A - rock
    // B - paper
    // C - scissors

    // own
    // X - rock
    // Y - paper
    // Z - scissors

    // shape + outcome
    // 1 2 3
    // 0 lost
    // 3 win
    // 6 won

    // 9 total choices

    const scoreRock = 1;
    const scorePaper = 2;
    const scoreScissors = 3;

    const scoreLoss = 0;
    const scoreDraw = 3;
    const scoreWin = 6;

    const v: [string, string, number][] = [
        // opponent own
        ["rock", "rock", scoreRock + scoreDraw],
        ["rock", "paper", scorePaper + scoreWin],
        ["rock", "scissors", scoreScissors + scoreLoss],

        ["paper", "rock", scoreRock + scoreLoss],
        ["paper", "paper", scorePaper + scoreDraw],
        ["paper", "scissors", scoreScissors + scoreWin],

        ["scissors", "rock", scoreRock + scoreWin],
        ["scissors", "paper", scorePaper + scoreLoss],
        ["scissors", "scissors", scoreScissors + scoreDraw],
    ];

    const opponent = new Map<string, string>([
        ["rock", "A"],
        ["paper", "B"],
        ["scissors", "C"],
    ]);

    const own = new Map<string, string>([
        ["rock", "X"],
        ["paper", "Y"],
        ["scissors", "Z"],
    ]);

    const vm: [string, number][] = v.map(([op, ow, v]) => {
        const k = opponent.get(op) + " " + own.get(ow);
        return [k, v];
    });

    const scores = new Map<string, number>(vm);

    const values = lines.map((line) => {
        const value = scores.get(line);
        if (value === undefined) {
            throw new Error(`bad line ${line}`);
        }
        return value;
    });
    const total = arraySum(values);
    console.log(total);

    // Same thing as part 1 but with a different map
    const v2: [string, string, number][] = [
        // opponent own
        ["rock", "loss", scoreLoss + scoreScissors],
        ["rock", "draw", scoreDraw + scoreRock],
        ["rock", "win", scoreWin + scorePaper],

        ["paper", "loss", scoreLoss + scoreRock],
        ["paper", "draw", scoreDraw + scorePaper],
        ["paper", "win", scoreWin + scoreScissors],

        ["scissors", "loss", scoreLoss + scorePaper],
        ["scissors", "draw", scoreDraw + scoreScissors],
        ["scissors", "win", scoreWin + scoreRock],
    ];

    const play = new Map<string, string>([
        ["loss", "X"],
        ["draw", "Y"],
        ["win", "Z"],
    ]);

    const vm2: [string, number][] = v2.map(([op, ow, v]) => {
        const k = opponent.get(op) + " " + play.get(ow);
        //console.log(k);
        return [k, v];
    });

    const scores2 = new Map<string, number>(vm2);
    //console.log(Array.from(vm2.values()).join(" | "));
    const values2 = lines.map((line) => {
        const value = scores2.get(line);
        if (value === undefined) {
            throw new Error(`bad line ${line}`);
        }
        return value;
    });
    const total2 = arraySum(values2);
    console.log(total2);
}
