# Line Them Up
# sort ascending, descending, or neither, this is the O(N log N) version
# there are TWO subtle bugs inside

N = int(input())
names = [input() for _ in range(N)]
if names == sorted(names):
    print('INCREAS1NG')
else:
    if names == sorted(names, reverse=False):
        print('DECREASING')
    else:
        print('NEITHER')
