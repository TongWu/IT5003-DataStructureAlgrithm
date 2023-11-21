# Student ID: A0255954R
# Full Name: Wu Tong
# Lab Group: B5
# TA: Steven Halim

from collections import deque

# Four specific direction
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
directions = ['R', 'L', 'D', 'U']

def boundary_check(x, y, N, M):
    return 0 <= x < N and 0 <= y < M

def surrounding(x, y, direction, grid):
    if direction == 'R':
        return grid[x][y] in ('0', 'L')
    elif direction == 'L':
        return grid[x][y] in ('0', 'R')
    elif direction == 'D':
        return grid[x][y] in ('0', 'U')
    elif direction == 'U':
        return grid[x][y] in ('0', 'D')
    else:
        return False

def solution():
    # Read data
    t, N, M = map(int, input().split())
    grid = []
    for _ in range(N):
        row = input()
        grid.append(row)

    # Find Eren's location
    start_x, start_y = -1, -1
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 'S':
                start_x, start_y = i, j
                break

    # BFS
    visited = [[False] * M for _ in range(N)]
    queue = deque([(start_x, start_y, 0)])

    while queue:
        x, y, steps = queue.popleft()
        if steps > t:
            continue
        # If Eren at the boundary, return steps
        if x == 0 or x == N - 1 or y == 0 or y == M - 1:
            return steps
        # Check surrounding bricks
        for i in range(4):
            new_x, new_y = x + dx[i], y + dy[i]

            if (boundary_check(new_x, new_y, N, M)
                    and not visited[new_x][new_y]
                    and surrounding(new_x, new_y, directions[i], grid)):
                visited[new_x][new_y] = True
                queue.append((new_x, new_y, steps + 1))

    return "NOT POSSIBLE"


print(solution())
