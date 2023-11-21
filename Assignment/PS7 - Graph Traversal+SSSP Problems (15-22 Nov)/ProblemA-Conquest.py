# Student ID: A0255954R
# Full Name: Wu Tong
# Lab Group: B5
# TA: Steven Halim

from sys import stdin
import heapq

def solution():
    # N for island number, M for bridge number
    N, M = map(int, stdin.readline().split())

    # Create a graph to store bridge
    graph = [[] for _ in range(N+1)]
    # Create a list to store army size
    army_size = [0] * (N+1)

    # Read bridge
    for _ in range(M):
        u, v = map(int, stdin.readline().strip().split())
        graph[u].append(v)
        graph[v].append(u)

    # Read army size
    for i in range(1, N+1):
        army_size[i] = int(stdin.readline().strip())

    # Initialize ds
    visited = [False] * (N+1)
    conquered = []
    heapq.heappush(conquered, (army_size[1], 1))
    visited[1] = True
    sn_army = army_size[1]
    unable_conquer = set()

    while conquered:
        _, island = heapq.heappop(conquered)
        for neighbor in graph[island]:
            if not visited[neighbor] and army_size[neighbor] < sn_army:
                #print(neighbor, army_size[neighbor])
                visited[neighbor] = True
                sn_army += army_size[neighbor]
                heapq.heappush(conquered, (army_size[neighbor], neighbor))
            elif not visited[neighbor] and army_size[neighbor] >= sn_army:
                unable_conquer.add(neighbor)

        new_conquer = set()
        for island in unable_conquer:
            if army_size[island] < sn_army:
                new_conquer.add(island)
                visited[island] = True
                sn_army += army_size[island]
                heapq.heappush(conquered, (army_size[island], island))

        unable_conquer -= new_conquer
    print(sn_army)

solution()