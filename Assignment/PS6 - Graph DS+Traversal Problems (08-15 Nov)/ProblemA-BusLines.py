# Student ID: A0255954R
# Full Name: Wu Tong
# Lab Group: B5
# TA: Steven Halim

def solution():
    # n for num of nodes
    # m for num of edges
    n, m = input().strip().split()
    n = int(n)
    m = int(m)

    # Check possibility
    if m > n * (n - 1) // 2:
        return "-1"

    edges_pair = []  # Path
    edges_sum = set()  # Path sum

    # Create spanning tree for vertices
    for i in range(2, n + 1):
        edges_pair.append((1, i))
        edges_sum.add(1 + i)
        m -= 1

    # Check if there still need to create edge
    if m > 0:
        # Select two nodes to pair the edge, judge the legality
        for i in range(2, n + 1):
            for j in range(i + 1, n + 1):
                edge_sum = i + j
                # If the edge sum is not in the set
                if edge_sum not in edges_sum:
                    # Add edge to list, add sum to set
                    edges_pair.append((i, j))
                    edges_sum.add(edge_sum)
                    m -= 1
                    if m == 0:
                        break
            if m == 0:
                break

    # Check again if still need to create edge
    if m != 0:
        return "-1"
    # Return all pairs
    return "\n".join(f"{node1} {node2}" for node1, node2 in edges_pair)


print(solution())
