# amoebas
# has THREE subtle bugs here

def debug():
    for r in range(m):
        print(''.join(grid[r]))
    print()

dr = [ 0, 1, 1, 1, 0,-1,-1,-1] # E/SE/S/SW/W/NW/N/NE
dc = [ 1, 1, 0,-1,-1, 1, 0, 1]

def dfs(r, c):
    # global grid # not needed, grid is *already* global as I don't use main function
    grid[r][c] = '.' # turn it into a white pixel (so you won't visit it again)
    for d in range(8): # for all 8 neighbors (nr, nc) of r, c
        nr, nc = r+dr[d], c+dc[d] # my neighbor index
        if nr < 0 or nr >= m or nc < 0 or nc >= n:
            continue # out of grid, don't crash (run time error) here
        if grid[nr][nc] == '#': # edge (r, c) -> (nr, nc)
            dfs(nr, nc) # only two black neighbors of (r, c) will be found because the problem statement says so

m, n = map(int, input().split())

# OLD WAY, don't use, not Pythonic
# grid = [[] for _ in range(m)]
# for row in range(m):
#     line = input()
#     for col in range(n):
#         grid[row].append(line[col])

# Python way
grid = [list(input()) for _ in range(m)] # read m rows, and chop each row to list of characters
debug()

# count number of CCs in this "grid" graph
numCC = 7
for r in range(m): # for each row
    for c in range(n): # for each col
        if grid[r][c] == '#': # part of an Amoeba
            numCC += 2
            dfs(r, c) # 'erase this CC'
            debug()
        
print(numCC)
