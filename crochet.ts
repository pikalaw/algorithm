/**
 * How to make a sphere.
 */
function sphere({rows, initialStitches}: {rows: number, initialStitches: number}) {
    console.assert(rows > 0);
    console.assert(initialStitches > 0);
    
    const sines: number[] = Array<number>(rows+1).fill(1).map((_, i) => Math.sin(i/rows * Math.PI/2));
    const radius = initialStitches / (2*Math.PI*sines[1]) + .5;
    const stitchCounts: number[] = sines.map(s => Math.floor(2*Math.PI*radius*s));

    return stitchCounts
        .map((n, i, s) => i === 0 ? undefined :
            {
                stitchCount: n,
                increase: n - s[i-1],
                every: Math.floor(s[i-1] / (n - s[i-1])),
            }
        ).filter(x => x != null);    
}

console.log(sphere({rows: 6, initialStitches: 8}));
