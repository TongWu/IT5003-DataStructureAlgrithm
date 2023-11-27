As everyone knows from last year, Eva and Stefán live in the Westman Islands. Back then, you helped Eva find the best itinerary to explore the whole country with Stefán in the shortest possible time. Now Eva wants to visit Egilsstaðir again, but on her trip around the country they found out that Stefán HATES single-lane bridges. Eva is looking to you again to help her keep Stefán in a good mood.

Can you help Eva find the way from the Westman Islands to Egilsstaðir that contains as few single-lane bridges as possible?
## Input
The first line contains two integers, 2≤n≤105, the number of positions, and n−1≤m≤min(2⋅10^5, n(n−1)/2), the number of roads. Next come m lines, each with 3 numbers 1≤a, b≤n and c∈{0,1} which means that there is a road that runs between place a and place b and contains a single-lane bridge if c=1, and a double-lane bridge if c=0. The Westman Islands will always be numbered 1 and Egilsstaðir will always be numbered n. You can assume that Iceland’s road system is coherent: it is possible to get to every place from every other place. You can also assume that each pair a,b appears at most once in the input.
## Output
Print one line with the smallest number of single-lane bridges that Stefán and Eva have to cross to reach the end of the route.

| Sample Input 1           | Sample Output 1 |
| ------------------------ | --------------- |
| `3 3 3 1 1 1 2 1 2 3 1 ` | `1 `            |

| Sample Input 2                             | Sample Output 2 |
| ------------------------------------------ | --------------- |
| `6 6 5 6 1 5 4 1 2 1 1 2 3 1 4 3 1 1 4 1 ` | `3 `            |

| Sample Input 3                                               | Sample Output 3 |
| ------------------------------------------------------------ | --------------- |
| `10 13 7 3 0 7 10 1 8 2 0 10 2 1 4 6 0 4 1 0 9 5 1 6 9 0 7 6 1 3 10 0 4 5 0 5 7 1 4 8 0 ` | `1`             |
