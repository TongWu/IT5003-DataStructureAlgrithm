# Student ID: A0255954R
# Full Name: Wu Tong
# Lab Group: B5
# TA: Steven Halim

import sys


def solution():
    def manhattan_distance(loc1, loc2):
        return abs(loc1[0] - loc2[0]) + abs(loc1[1] - loc2[1])

    # n for matrix size, k for dest number
    n, k = map(int, input().split())
    matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    # Each number's location
    dict = {i: [] for i in range(1, k + 1)}
    for i in range(n):
        for j in range(n):
            # If the number in matrix is in the range we possibly hop to
            if matrix[i][j] in dict:
                # Append to dict
                dict[matrix[i][j]].append((i, j))
    # If missing a required number, return -1
    for i in range(1, k + 1):
        if not dict[i]:
            print(-1)
            return
    minimum = float('inf')

    for loc_start in dict[1]:
        current_distance = 0
        # Check every route start from starting point
        for dest in range(1, k):
            current_distance += min(manhattan_distance(loc_start, loc_end) for loc_end in dict[dest + 1])
            if current_distance >= minimum: break
        minimum = current_distance
    print(minimum)


solution()
