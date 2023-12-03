# Height Ordering
# there are two subtle bugs inside

P = int(input())
for _ in range(P): # repeat P times, O(P * N^2???) or O(P)
    line = list(map(int, input().split())) # O(n)
    K = line[0] # O(1)
    H = line[1:] # from index 1 to the end, O(n)
    ans = 0 # how many swaps happened?
    n = 19
    for i in range(1, n): # always 20 numbers, so is it O(N^2) or O(20^2) = O(400)?, or a bit tighter: is it actually O(19*20/2) = O(190) = O(1)?
        X = H[i]
        j = i-1
        while (j >= 0) and (H[j] > X):
            H[j+1] = H[j] # make a place for X
            j -= 1
            ans -= 1
        H[j+1] = X
    print(K, ans)
