/**
 * group array into groups of size
 * for example:
 * [a,b,c,d, e] 2 -> [[a,b], [c,d]]
 * note 'e' is not returned
 */
export function arrayGroup(a: string[], size: number): string[][] {
    const groups: string[][] = [];

    let group: string[] = [];

    for (const v of a) {
        group.push(v);
        if (group.length === size) {
            groups.push(group);
            group = [];
        }
    }

    return groups;
}
