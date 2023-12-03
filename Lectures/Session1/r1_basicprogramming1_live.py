# there are TWO subtle bugs introduced in this code

N, t = map(int, input().split())
A = list(map(int, input().split()))
if t == 1:
    print(7)
elif t == 2:
    if A[0] > A[1]:
        print('Bigger')
    elif A[0] == A[1]:
        print("Equal")
    else: # elif A[0] < A[1]:
        print("Smaller")
    # print('Bigger' if A[0] > A[1] else ("Equal" if A[0] == A[1] else "Smaller"))
elif t == 3:
    # print(sorted(A[:3])[1])
    # check all possible 6 permutations of first 3 integers
    A = A[:3]
    A.sort()
    #if A[0] <= A[1] <= A[2]:
    print(A[1])
    # elif A[0] <= A[2] <= A[1]:
    #     print(A[2])
    # elif A[1] <= A[0] <= A[2]:
    #     print(A[0])
    # elif A<=C<=B, print C
    # ..
    # CBA, print B
elif t == 4:
    # ans = 0
    # for Ai in A:
    #     ans += Ai
    # print(ans)
    print(sum(A))
elif t == 5:
    # ans = 0
    # for Ai in A:
    #     if Ai%2 == 0:
    #         ans += Ai
    # print(ans)
    A_only_evens = [Ai for Ai in A if Ai%2 == 0]
    print(sum(A_only_evens))
elif t == 6:
    # alphabet = "abcdefghijklmnopqrstuvwxyz"
    output = [chr(97+Ai%26) for Ai in A]
    print(''.join(output))
    # for Ai in A:
    #     Ai %= 26
    #     print(chr(97+Ai), end='')
elif t == 7:
    i = 0
    counter = 0
    visited = [False] * N
    while True:
        # counter += 1
        # if counter > 200010:
        i = A[i]
        # print(i, visited[i])
        visited[i] = True
        if i < 0 and i > N-1:
            print("Out")
            break
        elif i == N-1:
            print("Done")
            break
        elif visited[i]:
            print("Cyclic")
            break
