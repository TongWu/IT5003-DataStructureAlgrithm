# Magic Sequence
# O(n^2) sort, O(n log n) sort, O(n) special counting sort (and stop here for IT5003 level)
# there are TWO subtle bugs inside

TC = int(input())
limit = 10**3+10
for _ in range(TC):
    N = int(input())

    A, B, C = map(int, input().split())
    S = [0]*N
    S[0] = A
    for i in range(1, N): # O(N)
        S[i] = (S[i-1] * B + A) % C
        
    # normal TimSort (MergeSort variant)
    # R = sorted(S) # this is O(n log n) Merge Sort

    # counting sort way
    freq = [0] * limit # prepare big frequency table
    for i in range(N): # O(N)
        freq[S[i]] += 1 # add one to the counter

    X, Y = map(int, input().split())
    V = 0

    # normal
    # for i in range(N): # O(N)
    #    V = (V * X + R[i]) % Y

    # counting sort way
    for i in range(limit): # 1 million steps :O
        for j in range(freq[i]): # echo i, freq[i] times, as simple as that
            V = (V * X + freq[i]) % Y
    
    print(V)
