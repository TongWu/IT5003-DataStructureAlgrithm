# sprinkled with a few bugs

from heapq import heappush, heappop
from math import inf

N, S, T = map(int, input().split())
D = [list(map(int, input().split())) for _ in range(N)] # AM of size N*N, in the problem statement, this AM is given name 'D'
# PS: Converting this AM input into AL doesn't really help

# now, run Dijkstra's from source S
# note that the source has to be from S because the weighted graph is assymetric: running the SSSP algorithm from T may not be the same as running the SSSP algorithm from S

# (Modified) Dijkstra's routine
dist = [inf for u in range(N)] # or [inf] * N
dist[S] = 0
pq = []
heappush(pq, (0, S))
# a bit shorter than the two lines earlier:
# pq = [(dist[S], S)] # dist[S] is usually (but not 100%) 0, so most people will start with pq = [(0, S)]

# sort the pairs by non-decreasing distance from s
while pq:                               # main loop
    d, u = heappop(pq)                  # shortest unvisited u
    # if d > dist[u]: continue            # a very important check (try turning it off to feel what will happen)
    for v in range(N):
        w = D[u][v]                     # all edges from u
        if dist[u]+w >= dist[v]: continue # not improving, skip
        dist[v] = dist[u]+w             # relax operation
        heappush(pq, (dist[v], v))  

# print what is the shortest path from S to T
print(dist[S])

# V is N in this problem
# But E is N^2 in this problem
# so O((V+E) log V) of Modified Dijkstra's on non-negative weights become O(N^2 log N) in this problem
# but N is only up to 1000 so this is fine

# For Nov 23 edition, Prof Halim actually discuss another variant/modification of Dijkstra's algorithm that can run in O(V^2) on dense graph (see the next code)
