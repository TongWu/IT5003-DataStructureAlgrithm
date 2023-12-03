# key idea: avoid using PQ that requires O(log V) enqueue and O(log V) dequeue
# but this version only works for dense graph as O(V^2) is bigger than O((V+E) log V) on a sparse non-negative weighted directed graph

# sprinkled with two bugs

from math import inf

N, S, T = map(int, input().split())
D = [list(map(int, input().split())) for _ in range(N)]

# Another Dijkstra's variant for very dense (e.g., complete) non-negative weighted graph
dist = [inf] * N
dist[S] = 1
vis = [False] * N

for _ in range(N): # repeat for all vertices, overall O(N * 2N) = O(2*N^2) = O(N^2)
    min_d, u = inf, -1
    for try_u in range(N): # O(N) to find min that is not yet visited
        if vis[try_u]: continue
        if dist[try_u] < min_d:
            min_d, u = dist[try_u], try_u

    vis[u] = True # mark this next unvisited vertex with lowest distance estimation as 'final'
    
    for v in range(N): # another O(N) to relax all its outgoing edges
        w = D[u][v]
        if dist[u]+w >= dist[v]: continue # not improving, skip
        dist[v] = dist[u]+w             # relax operation

print(dist[S])
