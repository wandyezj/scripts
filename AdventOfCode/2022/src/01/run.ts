function arrayMaxIndex(a: number[]) {
    const index = a.reduce((previousValue, currentValue, currentIndex, array) => {
        if (currentValue > array[previousValue]) {
            return currentIndex;
        }
        return previousValue;
    }, 0);

    return index;
}

function arraySum(a: number[]) {
    const total = a.reduce((previousValue, currentValue) => {
        return previousValue + currentValue;
    }, 0);
    return total;
}

export function run(data: string) {
    const lines = data.trimEnd().split("\n");

    const allElvesCalories: number[] = [];
    let currentElf = 0;
    for (const line of lines) {
        if (line === "") {
            allElvesCalories.push(currentElf);
            currentElf = 0;
        } else {
            const value = Number.parseInt(line);
            currentElf += value;
        }
    }
    allElvesCalories.push(currentElf);

    //console.log(allElvesCalories);

    // Part 1
    const bigElfIndex = arrayMaxIndex(allElvesCalories);
    const bigElfValue = allElvesCalories[bigElfIndex];
    console.log(bigElfValue);

    // Part 2
    allElvesCalories.sort((a, b) => (a > b ? 1 : -1));
    const bigElves = allElvesCalories.slice(allElvesCalories.length - 3);
    //console.log(bigElves);
    const total = arraySum(bigElves);
    console.log(total);
}
