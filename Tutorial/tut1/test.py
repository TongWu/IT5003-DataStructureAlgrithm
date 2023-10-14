def binary_search_left(cards, x):
    """Find leftmost position of x in sorted list, or where x should be inserted to keep the list sorted."""
    left, right = 0, len(cards) - 1
    while left <= right:
        mid = (left + right) // 2
        if cards[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return left


def binary_search_right(cards, x):
    """Find rightmost position of x in sorted list, or where x should be inserted to keep the list sorted."""
    left, right = 0, len(cards) - 1
    while left <= right:
        mid = (left + right) // 2
        if cards[mid] <= x:
            left = mid + 1
        else:
            right = mid - 1
    return right


def main():
    N = int(input().strip())
    cards = sorted(list(map(int, input().split())))

    Q = int(input().strip())
    for _ in range(Q):
        l, r = map(int, input().split())
        left_idx = binary_search_left(cards, l)
        right_idx = binary_search_right(cards, r)
        print(right_idx - left_idx + 1)


if __name__ == "__main__":
    main()
