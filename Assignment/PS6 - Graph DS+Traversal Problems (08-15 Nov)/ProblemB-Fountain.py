# Student ID: A0255954R
# Full Name: Wu Tong
# Lab Group: B5
# TA: Steven Halim

from collections import deque


def solution():
    def grid_boundary(x, y):
        # Determine the next pos in grid boundary or not
        return 0 <= x < n and 0 <= y < m

    n, m = map(int, input().split())
    grid = []
    # Read grid
    for _ in range(n):
        line = list(input().strip())
        grid.append(line)

    # BFS queue
    BFS_queue = deque()
    # Stone direction
    direction_stone = [(0, 1), (0, -1)]

    # Find water unit in the first line
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'V':
                BFS_queue.append((i, j))

    # BFS
    while BFS_queue:
        # Fetch a pos of water
        x, y = BFS_queue.popleft()
        # If the cell below is air
        if grid_boundary(x + 1, y) and grid[x + 1][y] == '.':
            # Change air to water
            grid[x + 1][y] = 'V'
            # Add this cell to BFS queue
            BFS_queue.append((x+1, y))
        # If the cell below is stone
        elif grid_boundary(x+1, y) and grid[x+1][y] == '#':
            # Check left and right side
            for offset_x, offset_y in direction_stone:
                new_loc_x, new_loc_y = x+offset_x, y+offset_y
                # Check boundary and cell is air
                if grid_boundary(new_loc_x, new_loc_y) and grid[new_loc_x][new_loc_y] == '.':
                    # Change to water
                    grid[new_loc_x][new_loc_y] = 'V'
                    # Add to BFS queue
                    BFS_queue.append((new_loc_x, new_loc_y))

    for row in grid:
        print(''.join(row))

    pass


solution()
