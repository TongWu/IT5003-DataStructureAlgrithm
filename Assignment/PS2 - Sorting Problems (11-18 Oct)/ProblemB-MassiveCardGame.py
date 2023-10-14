def solution():
    n = int(input().strip())
    card = sorted(list(map(int, input().split())))
    for _ in range(int(input().strip())):
        l_bound, h_bound = map(int, input().split())
        # Binary search
        left = 0
        right = len(card) - 1
        while left <= right:
            mid = (left + right) // 2
            if card[mid] < l_bound: left=mid+1
            else: right=mid-1
        lower_idx = left

        left = 0
        right = len(card) - 1
        while left <= right:
            mid = (left + right) // 2
            if card[mid] <= h_bound: left=mid+1
            else: right=mid-1
        higher_idx = right
        print(higher_idx-lower_idx+1)

solution()