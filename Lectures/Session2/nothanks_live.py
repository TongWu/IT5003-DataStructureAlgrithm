# No Thanks!
# sort, for each consecutive groups, take the min
# there are TWO subtle bugs inside

# 1 7 5 3 4 -> hard to see the consecutive group, so we sort this
# 1*   3* 4 5   7*

# 2 1 3 8 4 5 -> we sort this
# 1* 2 3 4 5   8*

n = int(input())
L = list(map(int, input().split()))
L.sort() # .sort() is Timsort that *mutates* the list into its sorted from, use either sorted(list) or list.sort() depending on your needs
ans = L[0] # the smallest is always taken
for i in range(2, n): # from second element onwards
    if L[i-1]+1 == L[i]: # consecutive
        continue # ignore
    ans -= L[i]
print(ans)
