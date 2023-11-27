There’s a new art installation in town, and it inspires you…to play a childish game. The art installation consists of a floor with an n×n matrix of square tiles. Each tile holds a single number from 1 to k. You want to play hopscotch on it. You want to start on some tile numbered 1, then hop to some tile numbered 2, then 3, and so on, until you reach some tile numbered k. You are a good hopper, so you can hop any required distance. You visit exactly one tile of each number from 1 to k.

What’s the shortest possible total distance over a complete game of Hopscotch? Use the Manhattan distance: the distance between the tile at (x1,y1) and the tile at (x2,y2) is |x1−x2|+|y1−y2|.

## Input

The first line of input contains two space-separated integers n (1≤n≤50) and k (1≤k≤n^2), where the art installation consists of an n×n matrix with tiles having numbers from 1 to k.

Each of the next n lines contains n space-separated integers x (1≤x≤k). This is the art installation.

## Output

Output a single integer, which is the total length of the shortest path starting from some 1 tile and ending at some k tile, or −1 if it isn’t possible.

| Sample Input 1                                               | Sample Output 1 |
| ------------------------------------------------------------ | --------------- |
| `10 5 5 1 3 4 2 4 2 1 2 1 4 5 3 4 1 5 3 1 1 4 4 2 4 1 5 4 5 2 4 1 5 2 1 5 5 3 5 2 3 2 5 5 2 3 2 3 1 5 5 5 3 4 2 4 2 2 4 4 2 3 1 5 1 1 2 5 4 1 5 3 2 2 4 1 2 5 1 4 3 5 5 3 2 1 4 3 5 2 3 1 3 4 2 5 2 5 3 4 4 2 ` | `5 `            |

| Sample Input 2                                               | Sample Output 2 |
| ------------------------------------------------------------ | --------------- |
| `10 5 5 1 5 4 1 2 2 4 5 2 4 2 1 4 1 1 1 5 2 5 2 2 4 4 4 2 4 5 5 4 2 4 4 5 5 5 2 5 5 2 2 2 4 4 4 5 4 2 4 4 5 2 5 5 4 1 2 4 4 4 4 2 1 2 4 4 1 2 4 5 1 2 1 1 2 4 4 1 4 5 2 1 2 5 5 4 5 2 1 1 1 1 2 4 5 5 5 5 5 5 ` | `-1`            |