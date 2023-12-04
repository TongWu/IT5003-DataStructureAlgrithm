# 1. Sorting

## O(n^2) Sorting

### Bubble Sort

```pseudocode
def BubbleSort(arr):
	n = len(arr)
    # 遍历所有数组元素
    for i in range(n): # O(n)
        # 标记此轮遍历是否进行了交换
        swapped = False
        for j in range(0, n - i - 1): # O(n)
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
```

-   迭代总数:$N\times (N-1)/2$
-   改进思路：如果我们在第二个循环中完全没有交换，则意味着数组已经排序完毕，此时可以停止Bubble Sort

### Selection Sort

```pseudocode
def selection_sort(arr):
    # 遍历所有数组元素
    for i in range(len(arr)):
        # 找到剩余未排序元素中的最小值
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
                
        # 将找到的最小元素交换到当前遍历的起始位置
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
```

### Insertion Sort

```pseudocode
def insertionSort(array A, integer N):
	for each element i in [1,...,N-1]:
		x = A[i]
		for j from 0 to i-1:
			if A[j] > x:
				A[j+1] = A[j]
			else: break
		A[j+1] = x
```

## O(NlogN) Sorting

### Merge Sort

```python
def merge_sort(arr):
    if len(arr) > 1:
        # 寻找中点，进行分解
        mid = len(arr) // 2
        L = arr[:mid]  # 获取左半部分
        R = arr[mid:]  # 获取右半部分

        # 递归地对半分进行分解
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        # 合并过程
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        # 检查是否有任何元素遗留在 L[] 和 R[] 中
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
```

# 2. Linked List



# 3. Binary (Max) Heap

-   最大二叉堆是一种特殊的**完全二叉树**，用于模拟**优先队列**。
    -   **完全二叉树Complete Binary Tree**：完整二叉树二叉树中的每一级（可能是最后一级/最低一级除外）都被完全填满，最后一级的所有顶点都**尽可能靠左**
    -   **优先队列Priority Queue**: 优先队列是一种特殊的队列，其中每个元素都有优先级。元素的添加是无序的，但是元素的删除是根据优先级进行的，优先级最高的元素首先被移除。
        -   `Enqueue`: 向队列添加一个元素。插入操作不考虑优先级，只是简单地添加元素到队列中
        -   `Dequeue`: 移除优先级最高的元素。如果有多个元素具有相同的最高优先级，则根据队列的具体实现，可以选择任何一个
        -   `Peek`: 查看优先级最高的元素，但不从队列中移除它
-   在最大二叉堆中，每个节点的值都**大于或等于**其子节点(child node)的值。这意味着堆的根节点(root node)总是最大的元素
-   对于包含$N$个元素的二叉堆，他的高度不会超过$log_2N$，因为这是一个完全二叉树

### (最大)二叉堆操作

-   `Create(A)`: $O(NlogN)$, 调用多次`Insert(v)`, 也有$O(N)$版本
-   `Insert(v)`: $O(logN)$
    -   在二叉最大堆中插入新项目 v 时，只能在最后一个索引 N 加 1 处进行，以保持紧凑数组 = 完整二叉树属性。然而，最大堆属性仍可能被违反。该操作将从插入点向上修复最大堆属性（如有必要），并在不再违反最大堆属性时停止。
-   `ExtractMax()`: $O(logN)$
    -   此操作提出并删除二叉堆中最大的元素(根节点)，并使用现有元素替代(为最后一个索引N)，然而此操作从根节点向下修复最大堆属性
-   `UpdateKey(i, new_v)`: $O(logN)$ 如果i已知
    -   需要向上和向下修复最大堆属性
-   `Delete(i)`: $O(logN)$ 如果i已知

## Python中的二叉堆

-   `import heapq`：`heapq`提供了**最小堆**的实现，如果需要实现最大堆，则可以将元素取反来实现。
-   `heapq.heappush(heap, item)`：将元素 `item` 添加到堆 `heap` 中。这会保持堆的不变性，即堆的第一个元素始终是最小的。
-   `heapq.heappop(heap)`：弹出并返回 `heap` 中的最小元素，同时保持剩余元素的堆不变性。
-   `heapq.heappushpop(heap, item)`：将 `item` 放入堆中，然后弹出并返回堆中的最小元素。这个操作比单独调用 `heappush` 和 `heappop` 更有效率。
-   `heapq.heapify(x)`：将列表 `x` 转换成堆，即重新排列列表 `x` 的元素，使其符合堆的性质。这是以线性时间运行的，非常高效

# 4. Binary Search Tree



# 5. HashTable

# 6. Graph

## Graph Data Structures

### Adjacency Matrix

-   邻接矩阵(AM)是一个正方形的矩阵，其中`AM[i][j]`表示从节点i到节点j的边的权重
    -   通常设置`AM[i][j]=0`来表示没有从i到j的边，然而如果图中包含值为0的加权边，则需要用其他符号(-1, None, NULL)表示无边
-   使用V*V的二维数组来实现此结构
-   空间复杂度为$O(V^2)$

### Adjacency List

-   邻接表(AL)是一个由V个列表组成的数组，每个节点有一个列表。对于每个顶点i,`AL[i]`存储i的邻居，可以存储(neighbour number, weight)对
-   使用向量对向量实现这种数据结构`AL = [[] for _ in range(N)]`
-   空间复杂度为$O(V+E)$，比AM要高效的多

### Edge List

-   边列表(EL)是边的集合，包括边所链接的节点和其权重。通常这些边是按权重递增排列的。
-   使用数组来实现`EL=[]`
-   空间复杂度为$O(E)$，比AL要高效的多

# 7. Graph Traversal

# 8. SSSP

