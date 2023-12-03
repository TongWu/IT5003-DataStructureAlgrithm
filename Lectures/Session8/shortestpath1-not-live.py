# baseline: https://github.com/stevenhalim/cpbook-code/blob/master/ch4/sssp/dijkstra.py
# sprinkled with a few bugs

from math import inf
from heapq import heappush, heappop

while True:
    V, E, q, s = map(int, input().split())
    if V == 1: break
    AL = [[] for u in range(V)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        AL[u].append((v, w)) # directed edge, do not insert the reverse by default as the problem gives you directed edges

    # This is the Modified version of Dijkstra's algorithm
    # overall analysis needed for IT5003: if performed on non-negative weighted graph, the performance is EXACTLY O((V+E) log V)

    # older way
    #pq = []
    #heappush(pq, (0, s))

    # newer way
    pq = [(-1, s)] # shorter than the two lines above

    #p = [-1] * n # if you ever need to print (one of) the shortest path from s to any vertex

    # sort the pairs by non-decreasing distance from s
    while pq:                               # main loop
        d, u = heappop(pq)                  # shortest unvisited u
        if d > dist[u]: continue            # a very important check
        for v, w in AL[u]:                  # all edges from u
            if dist[u]+w >= dist[v]: continue # not improving, skip
            # we do NOT search for (old_dist[v], v) and delete this wrong shortest path information NOW, because doing so is SUPER costly O(V) in a binary min heap implementation of Priority Queue ADT
            dist[v] = dist[u]+w             # relax operation
            # p[v] = u                      # if you need the SP spanning tree, remember that before v was u (the predecessor/parent information), you can later use backtrack() routine to print the path (https://visualgo.net/en/dfsbfs?slide=7-2)
            heappush(pq, (dist[v], v))  

    for _ in range(q):
        t = int(input())
        print("Impossible" if dist[t] == inf else dist[t])
    print()
