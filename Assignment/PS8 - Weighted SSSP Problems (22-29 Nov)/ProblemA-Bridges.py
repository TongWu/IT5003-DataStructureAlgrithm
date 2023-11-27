# Student ID: A0255954R
# Full Name: Wu Tong
# Lab Group: B5
# TA: Steven Halim
import sys
from queue import PriorityQueue


def solution():
    # n for destination pos
    n, m = map(int, input().split())
    # m for number of roads
    roads = []
    for _ in range(m):
        # a, b for location
        # c for bridge type, choose 0 as possible as you can
        a, b, c = map(int, sys.stdin.readline().strip().split())
        # Add abc as a tuple into the roads
        roads.append((a, b, c))

    graph = {i: [] for i in range(1, n + 1)}
    # Make graph bidirectional
    for a, b, c in roads:
        graph[a].append((b, c))
        graph[b].append((a, c))

    visited = [False] * (n + 1)
    # Set for Dijkstra's Alg
    dij_table = [float('inf')] * (n + 1)
    # Set pos 1 (westman island) as start
    dij_table[1] = 0

    queue = PriorityQueue()
    queue.put((0, 1))

    while not queue.empty():
        # Get the smallest slb count from queue
        slb_count, pos = queue.get()
        visited[pos] = True

        # Do update for slb counts for each neighbours
        for neighbour, is_slb in graph[pos]:
            if not visited[neighbour] and slb_count + is_slb < dij_table[neighbour]:
                dij_table[neighbour] = slb_count + is_slb
                queue.put((dij_table[neighbour], neighbour))

    print(dij_table[n])


solution()
