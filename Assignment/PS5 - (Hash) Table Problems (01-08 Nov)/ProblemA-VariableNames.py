# Student ID: A0255954R
# Full Name: Wu Tong
# Lab Group: B5
# TA: Steven Halim

import sys


def solution():
    N = int(input())
    desired = [int(sys.stdin.readline().strip()) for _ in range(N)]

    # Two hashmaps
    declared = {}
    attempt_count = {}

    for x in desired:
        if x not in declared:
            # If desired variable name is not declared, declare this name, count +1
            declared[x] = True
            attempt_count[x] = 1
            print(x)
        else:
            # If the desired name is taken, find the next available name
            while x * attempt_count[x] in declared:
                attempt_count[x] += 1
            c_x = x * attempt_count[x]
            declared[c_x] = True
            print(c_x)
            attempt_count[c_x] = 1


solution()
