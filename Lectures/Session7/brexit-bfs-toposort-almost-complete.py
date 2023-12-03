# brexit

# this is not complete yet
# you need to print the correct answer here (trivial last line)

# after that, it is also TLE :O
# the reason for that TLE is not yet discussed (hint: it is about avoiding cycle, if a country already leave, then... ??)

from collections import deque
from copy import deepcopy

# read input
C, P, X, L = map(int, input().split())
AL = [[] for _ in range(C)] # C vertices (countries)
degree = [0] * C # each country i has degree[i] trading partners
for _ in range(P): # for each edge (trading partner)
    A, B = map(lambda x: int(x)-1, input().split()) # in 0-based
    AL[A].append(B)
    AL[B].append(A) # bidirectional
    degree[A] += 1
    degree[B] += 1
    
original_degree = deepcopy(degree) # DEEPcopy this

# run Kahn's (BFS) algorithm modification
s = L-1
q = deque([s]) # L still in 1-based, -1 to 0-based
leave = [False] * C # all still in the Union
leave[s] = True # except the troublemaker
while q:
    u = q.popleft() # the one that leaves the union
    for v in AL[u]: # affecting neighbor v of u
        degree[v] -= 1 # one less trading partner
        if degree[v]*2 <= original_degree[v]: # less than or equal to half of original degree?
            q.append(v)
            leave[v] = True # v will also leave
