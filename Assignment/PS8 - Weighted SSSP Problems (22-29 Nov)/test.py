def hopscotch(matrix, n, k):
    # Create a list to store the coordinates of each number from 1 to k
    numbers = {i: [] for i in range(1, k + 1)}

    # Fill the numbers dictionary with coordinates of each number
    for i in range(n):
        for j in range(n):
            if matrix[i][j] in numbers:
                numbers[matrix[i][j]].append((i, j))

    # Check if it's possible to play the game
    for i in range(1, k + 1):
        if not numbers[i]:
            return -1  # If any number from 1 to k is missing, return −1.

    # Calculate the Manhattan distance for paths from 1 to k
    def manhattan_dist(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    # Initialize the minimum distance with a large number
    min_distance = float('inf')

    # Go through each number starting from 1 to k-1
    for start in numbers[1]:
        distance = 0
        for num in range(1, k):
            # Find the minimum distance to the next number
            distance += min(manhattan_dist(start, end) for end in numbers[num + 1])
            # If at any point distance exceeds current min_distance, break early
            if distance >= min_distance:
                break
        # Update the minimum distance if a shorter path is found
        min_distance = min(min_distance, distance)

    return min_distance


# Now we'll test the function with the provided sample input
sample_input_1 = [[5, 1, 3, 4, 2, 4, 2, 1, 2, 1],
                  [4, 5, 3, 4, 1, 5, 3, 1, 1, 4],
                  [4, 2, 4, 1, 5, 4, 5, 2, 4, 1],
                  [5, 2, 1, 5, 5, 3, 5, 2, 3, 2],
                  [5, 5, 2, 3, 2, 3, 1, 5, 5, 5],
                  [3, 4, 2, 4, 2, 2, 4, 4, 2, 3],
                  [1, 5, 1, 1, 2, 5, 4, 1, 5, 3],
                  [2, 2, 4, 1, 2, 5, 1, 4, 3, 5],
                  [5, 3, 2, 1, 4, 3, 5, 2, 3, 1],
                  [3, 4, 2, 5, 2, 5, 3, 4, 4, 2]]
n1, k1 = 10, 5

print(hopscotch(sample_input_1, n1, k1))
