# Rational Sequence 3
# simple complete binary tree traversal upwards (from N to root 1) and downwards (from 1 back to N)
# two subtle bugs here, understand the problem first

for _ in range(int(input())): # O(P * log N)
    K, N = map(int, input().split())
    
    # from N, go back to the root (starting from the root (1) to N directly is difficult)
    stack = []
    while N > 1: # O(log N) to go from N back to the root
        if N%2 == 0: # odd (I am a right child)
            stack.append('R')
        else:
            stack.append('L')
        N //= 2

    # from root, reconstruct the path back to N
    p, q = 1, 1
    while stack: # O(log N) to go from root 1/1 back to N
        cmd = stack[-1]
        stack.pop()
        if cmd == 'R':
            q = (p+q) # p remains
        else: # 'R'
            p = (p+q) # q remains

    print(K, ' ', p, '/', q, sep='')
