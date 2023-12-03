from itertools import permutations
from math import inf
import random
n = 10 # try changing this from 10 (a few seconds) to 11 (maybe a minute) to 12 (maybe 10 minutes), etc...
AM = [[random.randint(1, 99) for _ in range(n)] for _ in range(n)]
for i in range(n): AM[i][i] = 0
#n = 5
#AM = [[0, 24, 13, 13, 22], [24, 0, 22, 13, 13], [13, 22, 0, 19, 14], [13, 13, 19, 0, 19], [22, 13, 14, 19, 0]]
print(AM)
best_tour = inf
for p in permutations(range(n)):
    # print(p)
    cur = AM[p[-1]][p[0]] # last vertex back to vertex 0
    for i in range(n-1):
        cur += AM[p[i]][p[i+1]] # between successive vertices in the tour
    if cur < best_tour: # keep the current best
        best_tour = cur
        print(p, cur)
