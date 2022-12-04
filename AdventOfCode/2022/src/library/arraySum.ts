export function arraySum(a: number[]) {
    const total = a.reduce((previousValue, currentValue) => {
        return previousValue + currentValue;
    }, 0);
    return total;
}
