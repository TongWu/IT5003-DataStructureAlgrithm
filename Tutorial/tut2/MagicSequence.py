def s_com(N, A, B, C):
    S = [A]
    for i in range(1, N):
        nex = S[i - 1] * B + A
        if nex >= C: nex %= C
        S.append(nex)
    return sorted(S)


def hash_com(N, R, X, Y):
    V = 0
    for i in range(N):
        # V = (V * X + R[i]) % Y
        V = V * X + R[i]
        if V >= Y: V %= Y
    return V


def solution():
    TC = int(input())
    results = []

    for _ in range(TC):
        N = int(input())
        A, B, C = map(int, input().split())
        X, Y = map(int, input().split())

        S = s_com(N, A, B, C)
        R = radixSort(S, max(S))
        V = hash_com(N, R, X, Y)
        results.append(V)

    for i in results:
        print(i)


solution()
