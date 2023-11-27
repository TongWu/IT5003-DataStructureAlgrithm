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

    dp = [[float('inf')] * (n*n) for _ in range(k+1)]
    for (x, y) in dict[1]:
        dp[1][x*n+y] = 0

    # Dynamic Programming
    for number in range(2, k+1):
        for current in dict[number]:
            for previous in dict[number-1]:
                distance = manhattan_distance(previous, current)
                current_i = current[0]*n + current[1]
                previous_i = previous[0]*n + previous[1]
                dp[number][current_i] = min(dp[number][current_i], dp[number-1][previous_i]+distance)
    minimum = min(dp[k])

    print(minimum)
    return


solution()
