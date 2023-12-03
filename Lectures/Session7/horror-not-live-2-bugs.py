# Horror List
# sprinkled with a few subtle bugs
# in the recording, I showed you one bug, there is ONE other bug

from collections import deque
from math import inf # clean way to represent infinity in Python

N, H, L = map(int, input().split()) # N = vertices, L = edges
horror = list(map(int, input().split())) # H integers
AL = [[] for _ in range(N+1)] # N+1 vertices
for _ in range(L):
    a, b = map(int, input().split()) # already in 0-based
    AL[a].append(b)
    AL[b].append(a) # don't forget this if a<->b

for h in horror:
    AL[N].append(h)
    
s = N
q = deque([s])
dist = [inf] * (N+1) # dist = Horror Indices, they will be off by one in our method of adding a dummy super-source vertex
dist[s] = 0 # you can simulate this back to "correct" HI by setting dist[s] = -1
while q:
    u = q.popleft() # O(1) of deque
    for v in AL[u]:
        if dist[v] != inf: continue # some other path reach v first, ignore
        dist[v] = dist[u]-1 # add HI of v by 1 compared to HI of u
        q.append(v)

print(dist.index(min(dist)))
