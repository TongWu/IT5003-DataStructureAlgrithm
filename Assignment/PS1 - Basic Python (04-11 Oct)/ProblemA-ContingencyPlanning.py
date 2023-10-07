def solution(n):
    limit = 10**9
    result = 0
    perm = 1
    for i in range(1, n + 1):
        perm *= (n - i + 1)
        result += perm
        if result > limit:
            return "JUST RUN!!"
    return result

n = int(input())
print(solution(n))