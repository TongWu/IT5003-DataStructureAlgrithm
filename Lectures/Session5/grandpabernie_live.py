# grandapbernie
# two subtle bugs to avoid direct copy paste

from collections import defaultdict

trip = defaultdict(lambda : []) # if the country does not exist yet, create an empty list, this simplify our implementation
n = int(input())
for _ in range(n): # repeat n times, populate the database, O(n*1) = O(n)
    s, y = input().split() # split to country (short string, assume O(1)) and year
    y = int(y) # y must be treated as integer!!
    trip[s].append(y) # store s -> list of years

for k, v in trip.items(): # alpha be the chain length, the cost is O(alpha log alpha) per chain, alpha will be small
    k.sort() # sort the list of years ONCE, after I take note of ALL grandpa's trips
             # best case: n distinct country names, so each chain length = 1, O(n * 1 log 1) = O(n)
             # average: k distinct country names, each chain length is uniformly n/k, O(k * n/k log n/k) = O(n log n)
             # worst case: 1 country name only, one length of n years, O(n log n)
    
q = int(input())
for _ in range(q): # for each of the q queries
    s, k = input().split()
    k = int(k)+1
    # when is grandpa's k-th trip to s
    print(trip[s][k]) # O(1), don't forget to cast k to integer and take note of 1-based vs 0-based indexing
