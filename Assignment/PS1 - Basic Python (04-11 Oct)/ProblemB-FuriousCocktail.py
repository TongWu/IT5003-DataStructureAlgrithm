def solution(N, T, pos):
    pos.sort()
    pos.reverse()
    total = N * T
    for t in pos:
        total -= T
        if t - total <= 0:
            return "NO"
    return "YES"


num, drink_t = map(int, input().split())
pos = [int(input()) for _ in range(num)]
print(solution(num, drink_t, pos))