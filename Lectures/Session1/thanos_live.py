# there are two character bugs in this simple code

T = int(input())
for i in range(T):
    P, R, F = map(int, input().split())
    ans = 0
    while P < F: # still survive
        P += R
        ans += 1
    print(ans)
