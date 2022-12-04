export function arrayUnique(a: string[]): string[] {
    const unique = a.filter((value, index, array) => array.findIndex((x) => x === value) === index);
    return unique;
}
