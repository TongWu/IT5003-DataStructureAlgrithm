Nomads, Kingdoms, and Tribes are on the islands of the great seas. Bridges span between islands allowing travel between them. It is possible to get from every island to every other island through some sequence of bridges. The islands were at peace until everything changed when the Spanning Nation attacked!

Initially the Spanning Nation occupies island 1. From that point forward, the Spanning Nation can attack any island that is directly connected to some island already conquered by the Spanning Nation. Thankfully wars are resolved without any fighting. The Spanning Nation only attacks an island if the island’s army is strictly smaller than the Spanning Nation’s army. The smaller island army will simply concede and join the Spanning Nation’s army.

As the tactical advisor of the Spanning Nation, determine the maximum possible army size the Spanning Nation can have after making a series of attacks.

## Input

The first line contains the integer N (1≤N≤200000), which is the number of islands, and M (0≤M≤200000), the number of bridges.

The next M lines describe the bridges. Each of these lines contains two distinct integers u and v (1≤u,v≤N), indicating that there is a bridge between the islands u and v. There is at most one bridge between any pair of islands.

The next N lines describe the islands’ army size in order. Each of these lines contains a single integer s (0≤s≤1000), which is the army size of this island.

## Output

Display the maximum possible army size of the Spanning Nation.

| Sample Input 1                          | Sample Output 1 |
| --------------------------------------- | --------------- |
| `6 5 1 4 3 4 2 4 6 3 5 4 2 4 1 0 10 2 ` | `9 `            |

| Sample Input 2                         | Sample Output 2 |
| -------------------------------------- | --------------- |
| `6 5 3 4 3 1 2 3 6 1 5 3 2 3 0 1 3 3 ` | `3`             |