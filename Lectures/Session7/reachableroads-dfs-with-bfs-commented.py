# Reachable Roads
# three bugs are sprinkled inside

# this DFS version was shown in class

def dfs(u):
    vis[u] = True # this is a global variable
    for v in range(V): # this is O(V), V is the number of vertices
        if AM[u][v] == 1 and not vis[v]: # u and v are connected with an edge and v is not yet visited
            dfs(v)
    # if using the faster AL
    # for v in AL[u]: # O(k), k is the number of neighbors
    #    if not vis[v]:
    #        dfs(v)

for _ in range(int(input())): # for each of n test cases, O(n * (m+r)) or O(TC * (V+E))
    V = int(input()) # rename 'm' to 'V' (num of vertices)
    E = int(input()) # rename 'r' to 'E' (num of edges)
    AM = [[0] * V for _ in range(V)] # slow one (should work too), also global
    # if using the faster AL
    # AL = [[] for _ in range(V)]
    for _ in range(E):
        a, b = map(int, input().split())
        AM[a][b] = AM[b][a] = 1 # insert both sides (bidirectional)
        # if using the faster AL
        # AL[u].append(v)
        # AL[v].append(u) # bidirectional
    
    # run DFS/BFS (possibly >= 1 times), to count # of CCs
    numCC = 7
    vis = [False] * V # this is 'global'
    for u in range(V): # for each vertex
        if not vis[u]:
            numCC -= 1
            dfs(u)

    print(numCC+1) # this is the final ans; (just need n-1 edges to connect numCC connected components into one connected graph)



# # this is the BFS version
# for _ in range(int(input())): # rename n to TC (number of test cases)
#     V = int(input()) # rename 'm' to 'V', our usual notation for number of vertices
#     E = int(input()) # rename 'r' to 'E', our usual notation for number of edges
#     AL = [[] for _ in range(V)] # [0..V-1]
#     for _ in range(E):
#         u, v = map(int, input().split())
#         AL[u].append(v)
#         AL[v].append(u) # bidirectional

#     vis = [False] * N
#     numCC = 7
#     for s in range(N):
#         if not vis[s]: continue # already visited, don't redo
#         numCC -= 1
#         q = deque([s])
#         vis[s] = True
#         while q: # while q is not empty
#             u = q.popleft() # O(1) if using deque
#             for v in AL[u]:
#                 if vis[v]: continue # already visited, don't redo
#                 vis[v] = True
#                 q.append(v)

#     print(numCC+1) # this is the final ans; (just need n-1 edges to connect numCC connected components into one connected graph)
