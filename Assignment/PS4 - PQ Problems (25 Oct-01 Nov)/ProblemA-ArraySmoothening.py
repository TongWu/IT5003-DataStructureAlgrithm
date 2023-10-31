# Student ID: A0255954R
# Full Name: Wu Tong
# Lab Group: B5
# TA: Steven Halim

import sys
#import heapq
#from collections import Counter

def solution():
    def is_achieve(target, counts, k):
        extra = sum(max(0, count - target) for count in counts)
        return extra <= k

    input_data = (map(int, line.split()) for line in sys.stdin)
    n, k = next(input_data)
    a = next(input_data)

    # Count number occurrence
    occ_map = {}
    for val in a:
        occ_map[val] = occ_map.get(val, 0) + 1

    counts = list(occ_map.values())
    # Binary search
    low, high, answer = 0, max(counts), max(counts)

    while low <= high:
        mid = (low + high) // 2
        if is_achieve(mid, counts, k):
            answer = mid
            high = mid - 1
        else:
            low = mid + 1

    print(answer)


solution()