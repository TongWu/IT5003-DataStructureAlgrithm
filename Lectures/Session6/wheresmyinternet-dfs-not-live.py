# Where's My Internet??
# focusing only on DFS
# sprinkled with A FEW subtle bugs

def dfs(u):
    vis[u] = True
    for v in AL[u]: # for each neighbor v of u
        if not vis[v]: continue # if v already visited, skip
        dfs(v) # if I can reach this line, visit v
    
import sys
sys.setrecursionlimit(10**6) # just make it as big as N (or much more, to be very safe), e.g., # 1-2-3-4....-N (N-1)

N, M = map(int, input().split())
# AM = [[0] * N for _ in range(N)] # O(N^2) memory :O, (2*10^5)^2 = 4*10^10 = 40*10^9 (about 40 Giga cells)... boom...
AL = [[] for _ in range(N)] # use AL :)
for _ in range(M):
    # a, b = map(int, input().split())
    # a = a-1 # standard
    # b -= 1 # shorter
    # a, b = a-1, b-1 # combined
    a, b = map(lambda x: int(x)+1, input().split()) # cleanest: convert to integer and go to 0-based indexing
    AL[a].append(b)
    AL[b].append(a) # you forget this, Wrong Answer

# DFS from 1 (but now vertex 0)
vis = [False] * N # Direct Addressing Table of size N, 0-based
dfs(0) # house 1 in 0-based indexing is house 0

if all(vis): # all vertices are visited (all True)
    print("Connected")
else:
    for u in range(N):
        if not vis[u]:
            print(u+1) # print in 1-based
