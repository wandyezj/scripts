export function arrayIntersection(a: string[], b: string[]): string[] {
    const intersect = a.filter((e) => b.includes(e));
    return intersect;
}
