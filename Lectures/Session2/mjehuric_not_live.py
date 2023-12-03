# Mjehuric
# there are two subtle bugs inside

n = 4
a = list(map(int, input().split())) # O(n)
for i in range(n): # O(n*n^2) = O(n^3), or is this O(125), or even tighter O(25*24/2 * 5) = O(10 * 5) = O(50) = O(1)?
    for j in range(n-1): # O(n*n) = O(n^2)
        if a[j] < a[j+1]: # if bigger
            a[j], a[j+1] = a[j+1], a[j] # yes, Python can do this
            print(*a) # yes, Python can do this, is this O(1)? -> no, this is O(n)... but n always 5 for this problem...
