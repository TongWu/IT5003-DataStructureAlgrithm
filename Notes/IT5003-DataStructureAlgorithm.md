# 0 - Introduction

## 0.1 Analysis of Algorithms

### 0.1.1 Big-$O$ Notation

Big-$O$ notation represents the time and space complexity of an algorithm, it represents the upper bound of the function’s growth rate.

- $O(1)$: Constant. Whatever the input data size, the time/space complexity of the algorithm is fixed
- $O(n)$: Linear. The time/space complexity will increase proportionally with the input data size
- $O(log\ n)$: Logarithm. When input data size increase, the time/space complexity of the algorithm will increase, but it the increasing rate is decreasing
- $O(n^2)$, $O(n^3)$: The time/space complexity will increase square/cubic with the input data size.
- $O(2^n)$, $O(n!)$: Exponential and factorial. The time/space complexity will become huge when size of input increasing

Mathematically, an algorithm A is of O(**f(n)**) if there exist a constant **k** and a positive integer **n0** such that algorithm A requires no more than **k\*f(n)** time units to solve a problem of size **n ≥ n0**, i.e., when the problem size is larger than **n0**, then algorithm A is (always) bounded from above by this simple formula **k\*f(n)**.

![Big-O Notation](https://images.wu.engineer/images/2023/10/23/big_O_notation.png)

![Common Growth Terms](https://images.wu.engineer/images/2023/10/23/growth_rates.png)

# 1 - Sorting

## 1.1 Comparison-based sorting algorithms

### 1.1.1 Bubble Sort

> 冒泡排序（Bubble Sort）是一种简单的排序算法。这个算法会遍历要排序的数列，每次比较两个相邻的元素，如果它们的顺序（如从小到大、或从大到小）错误就把它们交换过来。遍历数列的工作会重复地进行，直到再没有需要交换的元素为止，也就是该数列已经排序完成。
>
> 这是一个逐步完善的过程 —— 在每一轮遍历中，“最重”的元素会像气泡一样“冒”到数列的一端。
>
> 冒泡排序的基本步骤如下：
>
> 1. 比较相邻的元素。如果第一个比第二个大（升序排序），就交换它们。
> 2. 对每一对相邻元素做同样的工作，从开始第一对到结尾的最后一对。在这一点，最后的元素应该会是最大的数。
> 3. 针对所有的元素重复以上的步骤，除了最后一个。
> 4. 持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。

#### Steps:

1. Compare the neighboring elements. If the first element is larger than the second, swap them
2. Do the same comparing (step 1) to each pair of neighboring elements, from the start one to the end one.
   - The iteration time for this will be smaller and smaller, since the sorted part is increasing
3. Do in a loop that iterates $N$ times

#### Code

```python
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

#### Time Complexity

$O(n^2)$, where $n$ is the number of element in the input.

### 1.1.2 Selection Sort

> 选择排序（Selection Sort）是一种简单直观的排序算法。它的工作原理是不断地选择剩余元素中的最小（或最大）者，放到排序序列的起始位置，直到所有的元素都已经排序完毕。这个算法分为已排序区间和未排序区间，不断地减少未排序区间的大小，同时增加已排序区间的大小，直到未排序区间为空。
>
> 选择排序的基本步骤如下：
>
> 1. 首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置。
> 3. 以此类推，直到所有元素均排序完毕。

#### Steps:

1. Found the minimum(maximum) element from the unsorted part, store it into the start
1. Continue find the minimum(maximum) element from the unsorted part, store it into the end of the sorted part

#### Code

```python
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

# 示例用法
my_list = [64, 25, 12, 22, 11]
selection_sort(my_list)
print("排序后的数组：", my_list)

```

#### Time Complexity

Since there are $n$ elements of number so the loop will iterate $n$ times, for each iteration we need to find the maximum or minimum element, which costs $O(n)$. So the time complexity should be $O(n^2)$

### 1.1.3 Merge Sort

> 归并排序（Merge Sort）是一种有效的、稳定的排序算法，它遵循分而治之的原则。这个算法主要依赖于将两个已经排序的列表合并成一个新的有序列表。
>
> 这里是归并排序的基本步骤：
>
> 1. **分解**：首先，列表从中间被分成两半，创建两个子列表。这一过程会递归继续，直到子列表只包含一个元素停止。一个元素的列表被认为是已排序的。
> 2. **合并**：接着，开始合并这些子列表，以创建多个较小的已排序列表，最终合并成一个单一的已排序列表。在合并过程中，会持续地将最小的元素从子列表中选出来，放入新的已排序列表中，直到所有的子列表都为空。

#### Steps:

1. Split the input list to 2 sub-list. This process will continue recursively until each sub-list only contain 1 element
2. Combine the sub-list, when combining, sort them

#### Code

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
# 使用示例
my_list = [12, 11, 13, 5, 6, 7]
print("原始数组：", my_list)
merge_sort(my_list)
print("排序后的数组：", my_list)

```

#### Time Complexity

Since the merge sort use divide & conquer method, the input list which has $n$ element has been split to many sub-list contains only 1 element and merge them. So the time complexity should be $nlog\ n$

### 1.1.4 Quick Sort

> 快速排序的基本思想是这样的：
>
> 1. **选择基准值：** 在列表中选择一个元素作为"基准"（pivot）。
> 2. **分区操作：** 所有比基准值小的元素摆放在基准前面，所有比基准值大的元素摆在基准的后面（相同的数可以到任何一边）。在这个分区结束之后，该基准就处于数列的中间位置。这个称为分区（partition）操作。
> 3. **递归地对基准值前后的子序列进行分区操作：** 递归地将前两步骤应用于更小的子序列。
>
> 重要的细节是，快速排序不是一个稳定的排序算法，也就是说，多个相同的值的相对位置也许会在算法结束时产生变动。
>
> 快速排序非常高效，对于大型数据集也非常有效。它的平均时间复杂度和最好情况下的时间复杂度都是 O(n log n)，但在最坏情况下的时间复杂度是 O(n^2)。然而，通过智能地选择基准元素，可以大大减少最坏情况发生的可能性。在实践中，由于其内部循环（inner loops）往往比其他排序算法的相应循环更短，快速排序通常比其他的 O(n log n) 算法更快。
>
> 此外，快速排序通常采用递归方式实现，这可能导致对于非常大的数据集，栈空间的消耗也是一个考量因素。不过，通过使用尾递归优化等技术，可以减少递归所需的栈空间。

#### Steps:



#### Time Complexity



#### Code



### 1.1.5 Random Quick Sort

> "Random Quick Sort" 是快速排序（Quick Sort）的一个变种，这种算法在快速排序的基础上增加了随机性，以解决标准快速排序在处理特定数据集（如已排序的数据）时效率低下的问题。其基本思想是随机选择基准元素，而不是简单地选择固定位置的元素（如第一个元素、最后一个元素或中间元素）。
>
> 下面是Random Quick Sort的基本步骤：
>
> 1. **选择基准：** 首先，在待排序的数组中随机选择一个元素作为基准（pivot）。
> 2. **分区：** 接下来，将数组分为两部分，一部分包含小于基准的元素，另一部分包含大于或等于基准的元素。这一步骤称为分区（partitioning）。
> 3. **递归：** 然后，递归地对两个子数组进行快速排序，直到子数组的大小为1或0，表示这些子数组已经排序好了。
>
> 引入随机选择基准的优势在于，它降低了算法在面对某些特定数据集时表现不佳的可能性。例如，在普通的快速排序中，如果数据已经排序，且我们总是选择第一个或最后一个元素作为基准，那么算法的效率会非常低下（因为这会导致每次分区最不理想的情况）。通过随机选择基准，我们期望算法的性能不会因输入数据的特定顺序而受到太大影响。
>
> 随机快速排序的平均时间复杂度通常仍为 O(n log n)，这使其成为非常有效的排序算法。然而，需要注意的是，在最坏的情况下，其时间复杂度仍然为 O(n^2)。不过，通过随机化基准元素的选择，这种最坏情况出现的概率会大大降低。

#### Steps:



#### Time Complexity



#### Code

### 1.1.6 Insertion Sort

> 插入排序（Insertion Sort）是一种简单直观的排序算法。它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描（对于单向链表则从前向后扫描），找到相应位置并插入。插入排序在实现上，在从后向前扫描过程中，需要反复把已排序元素逐步向后挪位，为最新元素提供插入空间。
>
> 具体来说，插入排序的算法步骤包括：
>
> 1. 将整个数列分为「已排序」和「未排序」两部分。初始时，「已排序」部分只有一个元素。
> 2. 从「未排序」的元素中，逐一取出元素插入到「已排序」部分，其位置是通过与「已排序」部分的元素逐一比较确定的。插入过程中，「已排序」部分的元素根据比较结果后移，为新元素腾出插入位置。
> 3. 重复上述过程，直到「未排序」部分元素全部插入「已排序」部分。
>
> 插入排序适用于少量数据的排序，时间复杂度为O(n^2)。它是稳定的排序算法，因为它保证了值相同的元素在排序后仍然保持原有的顺序不变。

## 1.2 Non Comparison-based Sorting Algorithms

### 1.2.1 Counting Sort

> 计数排序（Counting Sort）是一种非比较整数排序算法，意味着它不会比较待排序的元素。这种方法是基于对一组对象计数来确定排序后的位置。它适用于小范围的整数排序，并且效率非常高，时间复杂度可以达到O(n)。但是，它不适用于数值差距大的数据集，因为它需要的额外存储空间与待排序数据的具体值（不是数据的数量）成正比。
>
> 下面是计数排序的基本步骤：
>
> 1. **找出待排序的数组中最大和最小的元素**。
> 2. **统计数组：** 建立一个统计数组，利用索引来表示原始数组中的元素，用统计数组中的值来表示原始数组中对应元素的数量。具体而言，首先初始化一个计数数组，数组长度为原始数组最大元素和最小元素的差+1，所有位置的值都设为0。然后遍历原始数组，每遇到一个数，就在计数数组对应的位置上加1。
> 3. **累加数组：** 对统计数组做变形处理，累加前面的数，使得统计数组每个索引位置的值是对应值及其之前的所有数值的总和。这一步使得统计数组包含了位置信息，对于每个数而言，统计数组中对应值的部分表示了它在输出数组中应处的位置。
> 4. **输出结果：** 最后，倒序遍历原始数组，从统计数组找到正确位置，输出到结果数组。同时，每放置一个数到排序后的数组中，就将其对应的计数减少。
>
> 这种算法非常高效，尤其适用于最大和最小值之差不是很大，且重复值多的整数数组排序。然而，对于非整数排序，计数排序就需要修改和调整，因为它原生是不支持这样的数据类型的。此外，如果数值范围非常大，即使只有几个数，也可能因为需要大量空间来存储计数数组而变得不实际。

#### Steps:



#### Time Complexity



#### Code



### 1.2.2 Radix Sort

> 基数排序（Radix Sort）是一种非比较型整数排序算法，其方法是通过分配和收集来利用整数的内部结构实现排序。基数排序不是通过比较数值来排序，而是通过按数字级别分配桶来实现排序，每个级别的排序可以采用不同的排序算法。一般情况下，对于十进制数，就会基于数位来进行排序，先从最低有效数字（比如个位）开始，一直到最高有效数字。
>
> 基数排序包括两种方法：
>
> 1. **LSD（Least Significant Digit first）：** 首先根据最低有效位进行排序，然后逐渐向最高有效位过渡。这是最常用的排序方法，因为它的稳定性保证了数字的正确排序。
> 2. **MSD（Most Significant Digit first）：** 首先根据最高有效位进行排序，然后逐渐向最低有效位过渡。这种方法常用于字符串或者较长的数字排序，因为它可以在完成高位排序后，递归地在较短的字符串或数字上应用排序算法。
>
> 基数排序的一般步骤如下（以LSD为例）：
>
> 1. **创建桶：** 首先，初始化一个足够数量的桶，每个桶代表一个特定的数位（例如，十进制数有10个桶，从0到9）。
> 2. **分配过程：** 按照从最低有效位开始的顺序，将每个数分配到对应的桶中。例如，如果是个位数，那么数字 "25" 将会被放入 "5" 号桶。
> 3. **收集过程：** 在每个位的分配结束后，从桶中按照顺序收集数值，这一过程会保持之前位数的排序状态。
> 4. **重复过程：** 然后，重复分配和收集的步骤，针对更高的位数，直至最高有效位。
>
> 基数排序的效率高，特别是当整数的范围相对较小，且数目较多时，其时间复杂度可以达到O(nk)，其中 "n" 是排序的项数，"k" 是数字的平均长度。但是，这种方法也有其局限性，比如它需要占用更多的空间来存储桶，并且只适用于可以分解为独立数位的数据类型（例如整数或定长字符串）。



#### Steps:



#### Time Complexity



#### Code



# 2 - Linked List

## 2.0 Array implementation

`get(i)`: return `A[i]`, $O(1)$

`search(v)`: check each index one by one to see if `A[i] == v`, best case $O(1)$, worst case $O(n)$

`insert(i, v)`: shift item from index i to the end, to `i+1` until `end+1`, then set `A[i] = v`, best case $O(1)$, worst case $O(n)$

`remove(i)`: shift item from i+1 to end, to i to end-1, overwriting old `A[i]`, best case $O(1)$, worst case $O(n)$

## 2.1 Linked List

![Linked List Illustration](https://images.wu.engineer/images/2023/10/24/ll_illustration.png)

Additional Variables:

- `head`: pointer points to `a0`
- `val`: the current number of elements N in the linked list
- `tail`: pointer points to `a(n-1)`

Operations:

- `get(i)`: only keep the head and tail pointers, the list traversal is needed. So it is much slower than array. Its running time is $O(n)$
- `search(v)`: can only search from head, since only `next` pointer to point the next element but not previous. $O(n)$
- `insert(i, v)`: four possibilities
  1. Insert to the head (before the current first item), $O(1)$
  2. An empty linked list, $O(1)$
  3. The position beyond the last (the current tail), $O(1)$
  4. The other positions of the linked list, $O(N)$
- `remove(i)`: three possibilities:
  1. The head, $O(1)$
  2. The tail, $O(N)$, since tail pointer need to be updated to the i-1 element, go to this element needs $O(N)$
  3. The other positions of the linked list, $O(N)$ 

## 2.2 Stack

![Stack Illustration](https://images.wu.engineer/images/2023/10/24/stack_illustration.png)

LIFO

`push`, `pop` are both $O(1)$

- `push` 会将元素加在栈顶
- `pop`会将栈顶的元素移除

### Postfix expression

- push operand to stack, pop first 2 operand if an operator pushed in
- 4 1 2 9 3 / \* + 5 \* +
  - ( 9/3 \* 2 + 1 ) \* 5 + 4 = 39

## 2.3 Queue

FIFO

`push`, `pop` are both $O(1)$

- `push` 会将元素加在末尾
- `pop`会将第一个元素移除

## 2.4 Doubly Linked List

Add `prev` pointer to linked list, make faster

## 2.5 Double-Ended Queue (Deque)

Can only search from head/tail, insert new item to head/tail, remove item from head/tail

# 3 - Binary Heap

## 3.1 Introduction

A Binary Max Heap is a complete binary tree that maintains the Max Heap property

Complete Binary Tree: Every level in the binary tree, except possibly the last/lowest level, is completely filled, and all vertices in the last level are as fat left as possible.

Max Heap Property: The parent of each vertex - except the root - contains value greater than (or equal to) the value of that vertex.

> 1. 完全二叉树（Complete Binary Tree）：在这种树中，除了最后一层可能没有完全填满外，其它每一层都是完全填满的，并且在最后一层，所有的节点都尽可能地靠左边。
> 2. 最大堆属性（Max Heap Property）：在这样的堆中，每个节点的值都大于或等于它的子节点的值。唯一的例外是根节点，因为它没有父节点。

## 3.2 Binary Heap Height

If we have a Binary Heap of $N$ elements, its height will not be taller than $O(log\ N)$.

## 3.3 Binary Max Heap Operations

### `Insert(v)`

Insertion of a new item **v** into a Binary Max Heap can only be done at the *last index **N** plus 1* to maintain the compact array = complete binary tree property. However, the Max Heap property *may* still be violated. This operation then fixes Max Heap property from the insertion point **upwards** (if necessary) and stop when there is no more Max Heap property violation.

- 将新项 v 插入到最大二叉堆中只能在最后一个索引 N 加 1 处完成 (N+1)，以保持紧凑数组 = 完整二叉树属性。
- 然而，最大堆属性仍然可能被违反。因此需要从插入点向上修复最大堆属性。
  - 向上修复最大堆属性被称为`ShiftUp`, `BubbleUp`或`IncreaseKey`
- 时间复杂度=$O(log\ N)$

### `create(A)` ($O(N\ log\ N)$)

**Create(A) - O(N log N)**: Simply insert (that is, by calling **Insert(v)** operation) all **N** integers of the input array into an initially empty Binary Max Heap one by one.

**Analysis**: This operation is clearly O(**N** log **N**) as we call O(log **N**) **Insert(v)** operation **N** times. Let's examine the 'Sorted example' which is one of the hard case of this operation (Now try the Hard Case - O(N log N) where we show a case where **A = [1,2,3,4,5,6,7]** -- please be patient as this example will take some time to complete). If we insert values in increasing order into an initially empty Binary Max Heap, then every insertion triggers a path from the insertion point (a new leaf) upwards to the root.

将输入数组的所有 N 个整数一一插入（即通过调用 Insert(v) 操作）到最初为空的最大二叉堆中

### `create(A)` ($O(N)$)

**Create(A) - O(N)**: This faster version of **Create(A)** operation was invented by Robert W. Floyd in 1964. It takes advantage of the fact that a compact array = complete binary tree and all leaves (i.e., half of the vertices — see the next slide) are Binary Max Heap by default. This operation then fixes Binary Max Heap property (if necessary) only from the last internal vertex back to the root.

**Analysis**: A loose analysis gives another O(**N**/2 log **N**) = O(**N** log **N**) complexity but it is actually just O(2***N**) = O(**N**) — details in the next few slides. Now try the Hard Case - O(N) on the same input array **A = [1,2,3,4,5,6,7]** and see that on the same hard case as with the previous slide (but not the one that generates maximum number of swaps — try 'Diagonal Entry' test case by yourself), this operation is far superior than the O(**N** log **N**) version.

- 即从数组长度的一半位置开始修复(`len(A)/2`)，递减直到第一个索引

### `ExtractMax()`

- 取出最大堆中最大的数值，对于一个合法的最大堆，为root节点。

- 将索引最后一位元素提升至root节点，并向下修复最大堆属性

  - 被称为`ShiftDown`, `BubbleDown`或`Heapify`，具体操作如下：

  1. 将索引最后一位元素提升至root节点
  2. 将root节点和其两个子节点中**较大的值**作比较，如果符合条件则替换
  3. 重复第二步骤，逐步向下修复最大堆属性

- 时间复杂度为$O(log\ N)$

### `UpdateKey(i, newv)`

For some Priority Queue applications (e.g., [HeapDecreaseKey in Dijkstra's algorithm](https://visualgo.net/en/heap/sssp?slide=7-3)), we may have to modify (increase or decrease) the priority of an existing value that is already inserted into a Binary (Max) Heap. If the index **i** of the value is known, we can do the following simple strategy: Simply update **A[i] = newv** and then call **both** **shiftUp(i)** and **shiftDown(i)**. Only at most one of this Max Heap property restoration operation will be successful, i.e., **shiftUp(i)**/**shiftDown(i)** will be triggered if **newv** >/< old value of **A[parent(i)]**/**A[larger of the two children of i]**, respectively.

- 如果值的索引`i`已知，则可以直接更新`A[i]=newv`
- 然后向上和向下修复最大堆属性
- 在知道索引的情况下，时间复杂度为$O(log/ N)$

### `Delete(i)`

1. 将该索引的值提升至root节点的值+1，使其成为最大堆中最大的数
2. 向上修复最大堆属性`ShiftUp`
3. 进行`ExtractMax()`操作

- 时间复杂度为$O(log\ N)$

## Key Point

- 判断一个最大堆是否合法的条件为，判断一个内部节点的是否大于其所有（一个或者两个）子节点
- 向最大堆中插入元素时，将元素插入到堆的末尾（即索引的最后一位），随后向上修复最大堆属性
- **MAXimum** number of **comparisons** between heap elements required to construct a max heap of 10 elements using the **O(n)** BuildHeap: $C=1.5N$ (rounding) (10 elements = 15, 11 elements = 16, 12 element = 16)
- Maximum number of swaps to construct max heap of N elements using $O(N)$: (N=9, 7) (N=10, 8) (N=11, 9) (N=12, 10)
- An array A of n distinct integers that are sorted in descending order forms a valid Binary Max Heap. Assume that A[0] is not used and the array values occupy index [1:n].
- Given a Binary Max Heap, calling ShiftDown(i) ∀i > heapsize/2 will never change anything in the Binary Max Heap.
- 

# 4 - Hash Table

## 4.1 Introduction

Hash table is a data structure to **map key to values**. It uses a **hash function** to map large or even non-integer keys into a small range of Integer indices.

Since the probability of two distinct keys colliding into the same index is relatively high, each of this potential collision needs to be solved to maintain the data integrity. There are several collision resolution: open addressing (Linear probing, quadratic probing, double hashing) and closed addressing (separate chaining)

> ### 封闭寻址（链地址法）
>
> 封闭寻址通常是指使用链表将具有相同哈希值的所有元素链接起来。在这种方法中，哈希表的每个槽位不直接存储值，而是存储指向一个链表的指针。所有映射到同一索引的元素都会被添加到对应索引位置的链表中。
>
> 当发生冲突时，即两个不同的键通过哈希函数计算出相同的索引时，第二个键的值将被添加到与该索引相关联的链表的末尾。查找时，你需要遍历对应的链表来找到正确的键值对。
>
> ### 开放寻址
>
> 开放寻址不使用链表来存储冲突的元素，而是寻找哈希表中的下一个空槽位。当一个键通过哈希函数映射到一个已经被占用的索引时，哈希表会按照某种系统的方式（探测序列）来查找另一个空槽位。
>
> 开放寻址的几种常见方法包括：
>
> 1. **线性探测（Linear Probing）：** 当发生冲突时，按照线性序列（如+1，+2，+3...）探查下一个空位。
> 2. **二次探测（Quadratic Probing）：** 探查序列不是线性的，而是二次的（如+1，+4，+9...）。
> 3. **双重哈希（Double Hashing）：** 使用第二个哈希函数来决定探查序列。
>
> 开放寻址的一个优点是它不需要额外的存储空间来维护指针或链表。但缺点是当哈希表变得越来越满时，冲突的概率增加，这会降低表的性能。因此，需要合理的再哈希或扩容策略来维护效率。
>
> 在选择使用哪种方法时，通常会考虑多种因素，比如键值对的数量、表的大小、存储空间的限制、预期的查找/插入/删除操作的频率等。封闭寻址更适合元素数量较小或负载因子低的哈希表，而开放寻址适合数据量不大且平均占用空间较少的情况。

## 4.2 Direct Addressing Table

When the range of the Integer key is **small**, we can use initially empty (Boolean) array $A$ of size $M$ and implement the following table ADT operation directly:

- `search(v)`: check if `A[v]` is true (filled) or false (empty)
- `insert(v)`: Set `A[v]` to be true (filled)
- `remove(v)`: set `A[v]` to be false (empty)

All of these three operations has time complexity of $O(1)$, since it access the specific index of an array

> 在直接寻址表中，当你有一个键的集合K和这个集合中的每个键都是从0到某个最大整数m的整数时，你可以创建一个大小为m+1的数组A。数组的每个位置直接对应一个键，即如果你想要查找键k的值，你直接访问数组的第k个位置即A[k]。
>
> 这种方法的优点是简单且快速，操作的时间复杂度为O(1)，因为它只是直接访问数组的特定索引。但是直接寻址的缺点也很明显：
>
> - 如果键的范围非常大，你将需要一个非常大的数组，而实际上数组中的大部分空间可能都不会被使用，导致内存浪费。
> - 如果键的类型不是整数，或者是一组不连续的整数，则无法直接使用直接寻址。

### Satellite Data

We can add satellite data instead of just using a Boolean array to record the existence of the keys

For example:

`A[2] = 'SBS Transit'`

> 在直接寻址表中，每个槽位通常存储了一个元素及其关联的信息。这里的“卫星数据”指的是与每个键（或者说索引）相关联的那些附加信息。
>
> 例如，假设你有一个以人的ID号码为键的直接寻址表，用来存储人的详细信息。在这个表中，ID号码允许你直接访问存储在表中相应位置的数据。这个数据可能包含人的名字、地址、电话号码等信息。在这种情况下，名字、地址和电话号码就是与ID键相关联的卫星数据。
>
> 卫星数据的存在使得直接寻址表不仅仅可以作为简单的键值对存储结构，还可以存储和检索丰富的相关信息。在哈希表中也同样存在卫星数据的概念，其中每个键值对可能关联了一些额外的信息。无论在直接寻址还是在哈希表中，卫星数据都是你希望与键一起存储和查询的数据。

### DAT Limitation

1. The range of keys must be small. Otherwise the memory usage will be large
2. The keys must be dense, i.e., not many gaps in the key values. Otherwise DAT will contain too many empty (and wasted) cells
3. Can use hashing to overcome these restrictions

## 4.3 Hashing

Use hashing, we can:

1. Map some non-integer keys to integer keys
2. Map large integers to smaller integers

### Example

- For example, we have $N=400$ Singapore phone numbers (Singapore phone number has 8 digits, so there are up to $10^8=100M$ possible phone numbers in Singapore)
- Instead of using DAT (DAT needs an array with size $10^8$ which is so big), we can use the following simple hash function `h(v) = v % 997`
- This way, we map 8 digits phone numbers `6675 2378` and `6874 4483` into up to 3 digits `h(6675 2378) = 237` and `h(6874 4483) = 336`. Therefore, we only need to prepare an array of size $M = 997$ instead of $10^8$

### Hash Table Preview

With hashing, we can now implement the following Table ADT operations using Integer array (instead of Boolean array) as follows:

1. `search(v)`: check if `A[h(v)] != -1` (we use -1 for an empty cell assuming v>=0)
2. `insert(v)`: set `A[h(v)] = v` (we hash `v` into `h(v)` so we need to somehow record key `v`)
3. `remove(v)`: set `A[h(v)] = -1`

### Hash Table with Satellite Data

If we have keys that map to satellite data and we want to record the original keys too, we can implement the Hash Table using pair of `(integer, satellite-data)` arrays as follows

1. `search(v)`: return `A[h(v)]`, which is a `pair(v, satellite-data)`, possibly empty
2. `insert(v)`: set `A[h(v)] = pair(v, satellite-data)`
3. `remove(v)`: set `A[h(v)] = (empty pair)`

### Collision

> Fact:
>
> How many people (number of keys) must be in a room (Hash Table) of size 365 seats (cells) before the probability that some person **share a birthday** (collision, two keys are hashed to the same cell) becomes > 50 percent (i.e., more likely than not)?
>
> **A: 23 people (a small amount of keys) in the room (Hash Table) of size 365 seats for a 50% chance collision to happen.**

## 4.4 Hash Function

How to create a good hash function:

1. Fast to compute $O(1)$
2. Uses as minimum slots/Hash Table size $M$ as possible
3. Scatter the keys into different base addresses as uniformly as possible
4. Experience as minimum collisions as possible

### Perfect Hash Function

A perfect hash function is a one-to-one mapping between keys and hash values, i.e., no collision at all. It is possible if all keys are known beforehand

### Hashing Integer - Best Practice

`h(v) = v % M`

Map `v` into Hash Table of size `M` slots. The (%) is a modulo operator that gives the remainder after division. The time complexity is $O(1)$

The Hash Table size $M$ is set to be a reasonably large prime number, and not near a power of 2, about 2+ times larger than the expected number of keys $N$ that will ever be used in the Hash Table. This way, the load factor $\alpha = N/M <0.5$. 

Having low load factor, thereby sacrificing empty spaces, help improving Hash Table performance.

### Hashing String - Best Practice

```c
int hash_function(string v) { // assumption 1: v uses ['A'..'Z'] only
  int sum = 0;                // assumption 2: v is a short string
  for (auto& c : v) // for each character c in v
    sum = ((sum*26)%M + (c-'A'+1))%M; // M is table size
  return sum;
}
```

## 4.5 Collision Resolution

There are two main idea to resolve collision:

1. Open Addressing: All hashed keys are located in a single array. The hash code of a key code gives its base address. Collision is resolved by checking/probing multiple alternative addresses (hence the name open) in the table based on a certain rule.
2. Closed Addressing: The hash table looks like an Adjacency list (a graph data structure). The hash code of a key gives its fixed/closed base address. Collision is resolved by appending the collided keys inside an auxiliary data structure (usually any form from of List ADT) identified by the base address.

> ### 开放寻址：
>
> 与封闭寻址（Separate Chaining）使用链表来存储冲突的元素不同，开放寻址会在哈希表数组本身的其他位置寻找空槽位来存放冲突的元素。这意味着所有的元素都存储在哈希表的数组里，没有外部结构。
>
> 在开放寻址哈希表中，当发生哈希冲突时，元素可能会被存储在不是由哈希函数直接计算得到的槽位上。为了能够正确地查找元素，开放寻址策略采用一种称为“探测序列” (probing) 的机制。探测序列定义了在冲突发生时，如何顺序地检查哈希表中的其他槽位。
>
> 以下是在开放寻址哈希表中进行查找时的基本步骤：
>
> 1. **计算哈希值：** 使用哈希函数计算键的哈希值，得到初始索引位置。
> 2. **检查槽位：** 检查计算出的初始索引位置上的槽位。如果槽位为空，表示元素不在哈希表中；如果槽位中的键与要查找的键相匹配，则返回该槽位的内容。
> 3. **探测：** 如果初始槽位非空且其中的键不匹配，就使用探测函数来计算下一个槽位的位置。这里的探测函数可能是简单的线性探测（即逐个槽位地检查），也可能是二次探测（每次跳过更多的槽位），又或者是更复杂的双重哈希探测（使用第二个哈希函数确定探测间隔）。
> 4. **重复探测：** 重复步骤2和步骤3，直到找到一个空槽位（表示元素不在表中）或找到与查找键匹配的槽位。
> 5. **返回结果：** 如果找到匹配的键，则返回对应的值；如果遇到空槽位，则表示元素不在哈希表中，返回查找失败。
>
> #### **极端情况**
>
> 在开放寻址哈希表中，理论上每个槽位只存储一个元素。如果哈希表的槽位数量远小于数据集的大小，会导致一个高度集中的冲突情况，这种情况下开放寻址策略可能会非常低效。
>
> 在极端情况下，如果数据集的大小超过了哈希表的槽位数量，这种情况称为“哈希表已满”。一旦哈希表填满，就无法再插入新的元素，除非进行扩容操作（即增加槽位数量并重新散列现有元素），或者删除一些已存在的元素来释放槽位。
>
> 当哈希表的槽位数量有限，面对大数据集时，开放寻址会遇到如下挑战：
>
> 1. **探测次数增加：** 查找空闲槽位所需的探测次数会显著增加，这将导致插入操作变慢。
> 2. **聚集问题：** 特别是使用线性探测时，可能会发生聚集现象，即连续的槽位都被占用，这进一步增加了后续插入操作的探测次数。
> 3. **退化为线性搜索：** 在极端的负载情况下，如果几乎所有槽位都被占用，那么查找操作的性能可能会退化成线性搜索，时间复杂度接近O(N)。
>
> 在开放寻址中，并不存在一个槽位存储多个元素的情况。每个槽位只能存储单个元素，当该槽位发生冲突时，就必须通过探测找到另一个空闲槽位来存储该元素。如果没有空闲槽位，元素无法被插入到哈希表中。
>
> ### 封闭寻址：
>
> 封闭寻址通常是指使用链表将具有相同哈希值的所有元素链接起来。在这种方法中，哈希表的每个槽位不直接存储值，而是存储指向一个链表的指针。所有映射到同一索引的元素都会被添加到对应索引位置的链表中。
>
> 当发生冲突时，即两个不同的键通过哈希函数计算出相同的索引时，第二个键的值将被添加到与该索引相关联的链表的末尾。查找时，你需要遍历对应的链表来找到正确的键值对。
>
> 1. **插入（Insertion）：** 当你想插入一个键值对时，你会先使用哈希函数计算出键的哈希值，这个值将对应一个槽位索引。如果该槽位为空，则在那里插入一个新的链表，并添加键值对。如果槽位已经有了一个链表，则直接在链表的头部或尾部添加这个键值对。不同的实现可能会选择不同的插入策略（例如，头插法或尾插法）。
> 2. **查找（Search）：** 当查找一个键时，你同样会计算其哈希值以找到对应槽位的链表。然后，遍历这个链表，对比每个元素的键，直到找到匹配的键。因此，在查找时，你不需要知道键值对在链表中的位置，只需遍历链表直到找到或者遍历完整个链表。
> 3. **删除（Deletion）：** 删除一个键时，也是首先找到对应的链表，然后遍历链表以找到该键，接着将其从链表中移除。
>
> 

### Open Addressing

Discussing three OA collision resolution techniques: Linear Probing (LP), Quadratic Probing (QP), and Double Hashing (DH)

Let:

`M = HT.length ` 

- the current size of a Hash Table

`base = (key % HT.length)` 

- 这是基本的哈希函数，它将键值 `key` 映射到哈希表的一个槽位上。

`step = the current probing step ` 

- 这表示当前的探测步骤编号。在遇到冲突时，`step` 从 0 开始，每次探测递增。

`secondary = smaller_prime - key % smaller_prime (to avoid zero)` 

- 在双重哈希中用于计算第二个哈希值的表达式，其中 `smaller_prime` 是小于哈希表大小 `M` 的一个素数。通过从素数减去 `key` 对这个素数取模的结果，可以保证即使 `key` 能够被 `M` 整除，第二个哈希值也不会是零。



Linear Probing: `i = (base + step * 1) % M`

- 每次冲突，向当前索引加一，然后取模，确保结果在哈希表的范围内。

Quadratic Probing: `i = (base + step * step) % M`

- 每次冲突，增加的索引是当前步骤的平方，这有助于避免线性探测中的聚集问题。

Double Hashing: `i = (base + step * secondary) % M`

- 每次冲突，使用第二个哈希函数来计算增量，这通常能提供更好的散列分布，因为它结合了两个哈希函数的结果。

All three OA techniques require that the load factor $α = N/M < 1.0$ (otherwise no more insertion is possible). If we can bound α to be a small constant (true if we know the expected largest $N$ in our Hash Table application so that we can set up $M$ accordingly, preferably < 0.5 for most OA variants), then all Search(v), Insert(v), and Remove(v) operations using Open Addressing will be $O(1)$ — details omitted.

> 负载系数（Load Factor），通常用希腊字母$ α$（alpha）表示，在哈希表的上下文中，是一个衡量哈希表满度的指标。它定义为：
> $$
> \alpha = \frac nm
> $$
> 其中：
>
> - $n$ 是已经插入哈希表的元素数量。
> - $m$ 是哈希表中槽位的总数。
>
> 负载系数是一个重要的指标，因为它影响着哈希表操作的平均时间复杂度。在理想情况下（即没有冲突），哈希表的查找、插入和删除操作的时间复杂度可以是 O(1)。然而，由于哈希冲突的存在，这些操作的效率会随着负载系数的增加而降低。
>
> 在封闭寻址哈希（开放寻址哈希）中，当负载系数增加时，意味着空闲槽位减少，导致新元素插入时可能需要较多的探测步骤来找到空槽位，从而增加了冲突的可能性和解决冲突的成本。因此，为了保持操作的高效性，负载系数通常需要保持在一个相对较低的水平，例如小于 0.7 或 0.8。
>
> 在封闭寻址哈希（也称为链表哈希或分离链接哈希）中，负载系数的增加会导致存储在同一索引位置的链表平均长度增加，从而影响查找、插入和删除操作的效率。
>
> 因此，当负载系数达到某个阈值时，哈希表通常需要进行重新哈希（rehashing），即创建一个具有更多槽位的新哈希表，并将所有现有元素重新插入到新表中，以此降低负载系数，减少冲突，保持哈希表操作的效率。

### Closed Addressing (Separate Chaining)

- Use Doubly Linked List as auxiliary data structure, replace the slot element to a pointer point to the DLL
- If two keys `a` and `b` has the same hash value, they will append into the DLL’s head/tail ($O(1)$)
- The load factor is the average length of the $M$ lists

> - **链表**：哈希表中的每个槽位都与一个链表相关联。如果没有冲突，链表中只有一个元素。如果有冲突，所有具有相同哈希值的元素都将被添加到对应索引位置的链表中。
> - **插入操作**：当要插入一个新元素时，哈希函数首先确定这个元素应该位于哪个槽位。然后，这个元素被添加到该槽位的链表的头部或尾部。通常，链表的头部插入是最快的，因为这可以在 O(1) 的时间复杂度内完成。
> - **查找操作**：要查找一个元素，先通过哈希函数找到对应的槽位，然后在链表中遍历查找目标元素。
> - **删除操作**：删除操作也需要先找到元素所在的链表，然后在链表中找到并删除该元素。
> - **负载系数与性能**：尽管 separate chaining 允许负载系数超过 1.0，但一般建议保持在这个值以下，以维护操作效率。负载系数的增加会导致链表变长，从而影响查找和删除操作的性能。当链表平均长度较短时，即使是在冲突较多的情况下，这些操作的时间复杂度也可以接近 O(1)。
> - **重哈希**：随着元素的增加，为了维持效率，哈希表可能需要进行重哈希。这涉及创建一个更大的哈希表，并将所有元素重新散列到新表中。
>
> Separate chaining 的一个主要优点是它在处理冲突和维持性能方面相对宽容，尤其是在元素分布不均匀时。它的一个潜在缺点是可能会增加额外的内存开销，因为每个链表节点都需要额外的空间来存储指向链表下一个节点的指针。

> Separate Chaining is one method of Closed Addressing:
>
> 封闭寻址：
> 封闭寻址也称为开放散列，是一种处理散列表中碰撞的方法。当发生碰撞时，即两个键散列到相同的索引时，冲突会通过将值存储到表外来解决。哈希表中的每个位置通常以链接列表（或其他数据结构，如树形结构）的头部开始，所有哈希到相同位置的值都会插入到列表中。这样，哈希表本身永远不会 "满"，因为可以通过这些链表添加其他元素。
>
> 分离式链表
> 独立链式是一种特殊的封闭寻址方式。在分离式链表中，哈希表的每个槽都包含一个指向链表（或链）的链接，该链表包含哈希到同一槽的所有条目。当你想插入一个条目时，可以通过散列找到表中相应的槽，然后将其添加到该槽的列表中。与此类似，查找也需要对键进行散列，然后在列表中搜索相应的槽。
>
> 总结一下：
>
> - **闭地址法（Closed Addressing）**：当发生哈希冲突时，通过在哈希表外部存储元素来解决，每个槽位对应一个外部的数据结构。
> - **独立链表法（Separate Chaining）**：闭地址法的一种，每个哈希槽位链接到一个链表，所有散列值相同的元素都存储在这个链表中。

## 4.6 Linear Probing

In Linear Probing, we scan forwards one index at a time for the next empty/deleted slot (wrapping around when we have reached the last slot) when the collision occurs.

For example, let’s assume we start with an empty Hash Table `HT` with table size `M = HT.length = 7`, index 0 is `M-1 = 7-1 = 6`. Notice that 7 is a prime number. The primary hash function is simple, `h(v) = v%M`

> 线性探测（Linear Probing）是开放寻址策略下的一种简单冲突解决技术。当一个键的哈希索引位置已经被占用时，线性探测会尝试数组中的下一个位置，以此类推，直到找到一个空槽位。这种方法简单，但可能导致“聚集”问题，即连续的槽位被占用，从而可能需要多次探测来插入或查找一个元素。

### Insert

1. 使用哈希函数计算元素的哈希值，得到一个索引。
2. 检查哈希表中该索引位置是否为空。
3. 如果为空，则直接插入元素。
4. 如果不为空（发生冲突），则向下移动到下一个索引位置。
5. 重复步骤 3 和 4，直到找到空槽位为止。
6. 如果表已满，返回插入失败或者扩大哈希表进行重哈希。

### Search

1. 使用哈希函数计算元素的哈希值，得到一个索引。
2. 检查哈希表中该索引位置的元素是否为要搜索的元素。
3. 如果是，返回该元素或其位置。
4. 如果不是，检查该位置是否为空。
5. 如果不为空且不是目标元素，则移动到下一个索引位置。
6. 重复步骤 2 至 5，直到找到元素或遇到一个空槽位为止。
7. 如果找到一个空槽位，表示元素不在哈希表中，返回搜索失败。

### Remove

1. 使用哈希函数找到元素的索引位置。
2. 如果找到目标元素，将其删除并将该位置标记为“已删除”或使用特殊值（比如使用懒删除策略）。
3. 线性探测中的删除需要特别注意：不能简单地将位置设为空，因为这会断开后续探测链，导致在搜索和插入时错过后面的元素。
4. 在删除元素后，需要重新插入该位置后面的所有元素，直到遇到一个真正的空槽位，以确保探测链的连续性。

### Primary Clustering

We define a **cluster** to be a collection of consecutive occupied slots. A cluster that covers the base address of a key is called the **primary cluster** of the key.
我们将簇定义为连续占用槽的集合。覆盖键基地址的簇称为键的主簇。

Now notice that Linear Probing can create large primary clusters that will increase the running time of Search(v)/Insert(v)/Remove(v) operations beyond the advertised O(**1**).
现在请注意，线性探测可以创建大型主集群，这将增加 Search(v)/Insert(v)/Remove(v) 操作的运行时间，超出所宣传的 O(1)。

> 在哈希表的开放寻址冲突解决方法中，“主簇”（Primary Clustering）是指连续的已占用槽位形成的一组。这种情况特别是在使用线性探测方法时经常出现，因为一旦一个槽位被占用，后续发生冲突的元素会线性地探测下一个空槽位，导致连续的槽位被填充。
>
> 当主簇形成后，它可能会对哈希表的性能产生不利影响，因为插入和搜索操作可能需要更多的探测步骤来找到空闲槽或目标元素。在主簇内搜索一个不存在的元素会尤其低效，因为必须探测整个簇直到遇到一个空槽位。主簇越大，探测时遇到的平均冲突次数就越多，这就是为什么大的主簇会显著增加哈希表操作的平均时间复杂度。
>
> 为了减少主簇的影响，可以采取如下策略：
>
> 1. 使用二次探测或双重散列等非线性探测技术来分散连续的冲突。
> 2. 保持较低的负载因子，这样哈希表中有更多空槽位可供使用，减少冲突发生的机会。
> 3. 定期重新散列（Rehashing）哈希表以分散元素并减少簇的大小。
>
> 二次探测和双重散列是解决或减轻主簇问题的常用方法，因为它们在探测冲突时不是简单地按顺序检查下一个槽位，而是跳过一些槽位，降低了连续填充的可能性。

## 4.7 Quadratic Probing

To reduce primary clustering, we can modify the probe sequence to:

```c
h(v) // base address
(h(v) + 1*1) % M // 1st probing step if there is a collision
(h(v) + 2*2) % M // 2nd probing step if there is still a collision
(h(v) + 3*3) % M // 3rd probing step if there is still a collision
...
(h(v) + k*k) % M // k-th probing step, etc...
```

This quadratic probing, the probe jumps quadratically, wrapping around the Hash Table as necessary.

## 4.8 Double Hashing



## 4.9 Separate Chaining

Try Insert([9,16,23,30,37,44]) to see how Insert(v) operation works if we use Separate Chaining as collision resolution technique. On such random insertions, the performance is good and each insertion is clearly O(**1**).
尝试 Insert([9,16,23,30,37,44]) 看看如果我们使用分离链接作为冲突解决技术，Insert(v) 操作如何工作。在这种随机插入中，性能良好，并且每次插入显然都是 O(1)。



However if we try Insert([68,90]), notice that all Integers {68,90} are 2 (modulo 11) so all of them will be appended into the (back of) Doubly Linked List 2. We will have a long chain in that list. Note that due to the screen limitation, we limit the length of each Doubly Linked List to be at maximum 6.
然而，如果我们尝试 Insert([68,90])，请注意所有整数 {68,90} 都是 2（模 11），因此所有它们都将被追加到双向链表 2（的后面）中。我们将得到一个该列表中的长链。请注意，由于屏幕限制，我们将每个双向链表的长度限制为最大 6。

## 4.10 Extras



## Key Points

- Open Addressing (Linear Probing): 
  - 当发生哈希冲突时，向后寻找下一个空/已删除的槽位
  - 如果到达槽位末尾，则下一个寻找的目标为第一个槽位
  - 删除操作时，将该槽位设置为DEL，以防止在搜索时失去哈希冲突之连续性
  - “主簇”（Primary Clustering）是指连续的已占用槽位形成的一组，大的主簇会显著增加Hashmap操作的时间复杂度
- Closed Addressing (Separate Chaining): 
  - 当发生碰撞时，即两个键散列到相同的索引时，冲突会通过将值存储到表外来解决(对于Separate Chaining来说时DLL)。

| 控制字符 | ASCII值 | 控制字符 | ASCII值 |
| -------- | ------- | -------- | ------- |
| A        | 65      | a        | 97      |
| B        | 66      | b        | 98      |
| C        | 67      | c        | 99      |
| D        | 68      | d        | 100     |
| E        | 69      | e        | 101     |
| F        | 70      | f        | 102     |
| G        | 71      | g        | 103     |
| H        | 72      | h        | 104     |
| I        | 73      | i        | 105     |
| J        | 74      | j        | 106     |
| K        | 75      | k        | 107     |
| L        | 76      | l        | 108     |
| M        | 77      | m        | 109     |
| N        | 78      | n        | 110     |
| O        | 79      | o        | 111     |
| P        | 80      | p        | 112     |
| Q        | 81      | q        | 113     |
| R        | 82      | r        | 114     |
| S        | 83      | s        | 115     |
| T        | 84      | t        | 116     |
| U        | 85      | u        | 117     |
| V        | 86      | v        | 118     |
| W        | 87      | w        | 119     |
| X        | 88      | x        | 120     |
| Y        | 89      | y        | 121     |
| Z        | 90      | z        | 122     |

# 5 - Binary Search Tree

## Key Points

- BST(二分搜索树)中，某个顶点的左侧子树中的每个顶点必须小于该顶点值，而右侧子树中的每个顶点则必须大于该定点值

- Leaf Vertex：没有子顶点的顶点。Internal Vertex：有子顶点的顶点（root节点除外）

- Insert, Search, Remove操作都从root节点开始遍历，判断要插入/搜索/删除的值大于或小于当前节点

- Successor: 下一个比目标节点大的值。从左往右看BST，为目标节点的右边一个节点（无论上下）

- Predecessor: 上一个比目标节点小的值。从左往右看BST，为目标节点的左边一个节点（无论上下）

- Traversal：分为三种方式, Inorder, Preorder, Postorder

  ![image-20231107171436300](https://images.wu.engineer/images/2023/11/07/image-20231107171436300.png)

  - Inorder:

    1. 优先遍历root节点的左侧子树，在节点没有左侧和右侧字数的情况下访问该节点(5)
    2. 返回**并访问**至上一个节点(16)
    3. 遍历右侧的子节点，访问最底部节点(28)
    4. 循环执行步骤2，3
    5. 返回至root节点并访问(31)
    6. 遍历root节点的右侧子树，同时优先遍历右侧中的左侧子树
    7. 循环执行步骤2，3

    - 访问顺序: 5 -> 16 -> 28 -> 31 -> 49 -> 74 -> 99

  - Preorder:

    - 遍历顺序与inorder一致
    - 但是在遍历时就访问该节点，例如从root节点开始，故root节点被第一个访问
    - 访问顺序: 31 -> 16 -> 5 -> 28 -> 74 -> 49 -> 99

  - Postorder:

    - 遍历顺序与inorder一致
    - 但是在遍历时，只有在**当前节点没有子节点，或所有子节点都被访问过之后，才访问该节点**
    - 访问顺序: 5 -> 28 -> 16 -> 49 -> 99 -> 74 -> 31

- How many structurally different BSTs can you form with **n distinct** elements?
  $$
  \begin{aligned}
  C_n &= \frac 1 {n+1} {2n \choose n} = \frac {(2n)!} {(n+1)!\times n!} \\
  \end{aligned}
  $$

- What is the value of the element with **rank n** in this BST?

  - 从左往右看BST，为从左往右数的第N个节点（无论上下）

- What is the **minimum** possible height of a **BST** with **N** elements?
  $$
  \lfloor log_2N \rfloor
  $$
# 6 - Graph Structures
- Graph can be:
	- **undirected**: no distinction between two vertices associated with each bidirectional edge
	- **directed**: edges are directed from one vertex to another but may not directed from another direction
## 6.1 Simple Graph
- In simple graph:
	- no **self-loop edge**: edge that connects with itself
	- no **multiple/parallel edges**: edges between the same pair of vertices
	- There can only be **up to one edge** between a pair of distinct vertices.
- The *maximum number* of edges $E$ in a simple graph is $O(V^2)$
## 6.2 Terminologies
- **Incident and adjacent 相连和相邻**
	- Undirected edge $e: (u, v)$ is said to be **incident** (相连) with its two end-point vertices $u$ and $v$. 
	- Two vertices are called **adjacent** (相邻) (or neighbour) if they are incident with a common edge. For example, edge (0, 2) is incident to vertices 0 and 2, and vertices 0 and 2 are adjacent.
- **Adjacent edges 相邻边**
	- Two edges are called **adjacent** if they are incident with a **common vertex**. For example, edge (0, 2) and edge (2, 4) are adjacent.
- **Degree 顶点的度**
	- The **degree** of a vertex $v$ in an undirected graph is the number of edges incident with $v$. 
- **Subgraph 子图**
	- A **subgraph** $G'$ of graph $G$ is a smaller graph that contains subset of vertices and edges of $G$
	- 子图中的所有顶点都在原图的顶点集中，子图的所有边都在原图的边集中
- **Path and path length 路径和路径长度**
	- The **path** is a set of multiple edges from a specific vertex to another specific vertex. 
	- The **path length** is the number of vertex in the path. 
- **Simple path 简单图**
	- If there is no repeated vertex along the path, we call it as a **simple path**
- **Connected Graph 连通图**
	- An undirected graph $G$ is called **connected** if there is a path between every pair of distinct vertex of $G$
- **Connected Component 连通成分**
	- An undirected graph $C$ is called a **connected component** of the undirected graph $G$ if:
		1. $C$ is a subgraph of $G$
		2. $C$ is connected
		3. $C$ is the maximal subgraph that satisfies the other two criteria
- **Cut vertex/bridge 割点/桥**
	- A vertex/bridge that increase the graph's number of connected components if this vertex/bridge is deleted
	- 指在一个无向图中的一个顶点，当我们移除这个顶点以及与它相连的边后，原本连通的图变成了不连通的，即这个顶点的移除增加了图的连通分量的数量。
- **Adjacent for directed edge 有向边中的相邻顶点**
	- Suppose a *directed* edge $e: (u\to v)$, we say that $v$ is *adjacent to* $u$ but not in the other direction
- **In-degree and Out-degree 有向边中的入度和出度**
	- In-degree of $v$ is the number of edges coming into $v$
	- Out-degree of $v$ is the number of edges going out from $v$
- **Strongly Connected Component 有向图中的强连通成分
	- A directed graph $G$ is called **strongly connected** if there is a path *in each direction* between every pair of distinct vertices of $G$
	- A directed graph $SCC$ is called a **strongly connected component** of the directed graph $G$ if:
		1. $SCC$ is a subgraph of $G$
		2. $SCC$ is *strongly* connected
		3. No connected subgraph of $G$ has $SCC$ has a subgraph and contains vertices or edges that are not in $SCC$
			- i.e., $SCC$ is the maximal subgraph that satisfies the other two criteria
- **Cycle 循环**
	- A **cycle** is a path that starts and ends with the *same vertex*
- **Acyclic Graph 无循环图**
	- An **acyclic graph** is a graph that not contains any *cycle*
- **Trivial Cycle 平凡环**
	- In an *undirected graph*, each of its undirected edge causes a **trivial cycle** of length 2, we will not classify it as a cycle
- **Directed Acyclic Graph (DAG) 有向无环图**
	- A *directed graph* which is not acyclic has a special name: **directed acyclic graph (DAG)**
## 6.2 Special Graphs
### Tree
- Tree is a **connected graph** with $V$ vertices and $E=V-1$ edges
- **Acyclic**: does not contain any cycle
- Has *one unique path* between any pair of vertices
- Tree is usually defined on **undirected graph**
- Tree with one of its vertex designated as *root vertex* is called a **rooted tree**
- In a **rooted tree**, we have the concept of hierarchies (parent, children, ancestors, descendants), subtrees, levels, and height.
	- **Parent 父节点**
		- 每个节点（除了根节点）都有一个直接相连的上级节点称为其父节点
	- **Children 子节点**
		- 任何节点的直接下级节点称为它的子节点
	- **Ancestors 祖先**
		- 从根节点到达某个节点所经过的所有节点，**包括该节点本身**，都是这个节点的祖先
	- **Descendants 后代**
		- 任何节点下方的所有节点（无论距离多远）都是该节点的后代
	- **Subtrees 子树**
		- 任何节点**和**它的后代节点，连同它们之间的边，一起构成一个子树
	- **Levels 层**
		- 根节点位于第一层，其子节点位于第二层，以此类推。某个节点的层级数是从根节点到该节点的唯一路径上的边的数量加一
	- **Height 高**
		- 树的高度是树中任何节点的最大层级数。等价地，也可以定义为从该节点到其任何叶节点的最长路径的长度
- **Binary Tree** is a *rooted tree* in which a vertex has at most two children that are named *left child* and *right child*
- A **full binary tree** is a binary tree in which each non-leaf (also called internal) vertex has *exactly two children*
- A **complete binary tree** is a binary tree in which every level is completely filled, except possibly the last level may be filled as far *left* as possible.

### Complete Graph
- **Complete Graph** is a graph that there is an edge between *any* pair of vertices
- Complete graph is the *most dense* simple graph

### Bipartite Graph
- **Bipartite Graph** is an undirected graph with $V$ vertices that can be partitioned into two adjacent set of vertices of size $m$ and $n$ where $V=m+n$. 
- There is no edge between members of the same set.
- Bipartite graph is free from odd-length cycle
- Bipartite graph can be *complete*, i.e., all $m$ vertices from one disjoint set are connected to all $n$ vertices from the other disjoint set
- A *tree* is also a *bipartite graph*.

### DAG
- **Directed Acyclic Graph (DAG)** is a directed graph that has no cycle

## 6.3 Data Structures
### Adjacency Matrix, AM
- **Adjacency Matrix** is a square matrix where `AM[i][j]` shows the edge's weight from vertex `i` to `j`. For unweighted graphs, set unit weight =1 for all edge weights
- Usually set `AM[i][j]=0` to indicate there is no edge for $(i, j)$. However, if the graph contains 0-weighted edge, we have to use another symbol to indicate "no edge", like `-1, None, null`
- Use `VxV` 2D array/list to implement this data structure

- AM requires space complexity of $O(V^2)$

### Adjacency List, AL
- **Adjacency List** is an array of $V$ lists, each vertex has a list or hash table. The list/hash table contains all other vertices that directly connected to this vertex.
- AL has space complexity of $O(V+E)$, far more efficient than AM
- AL is *efficient* especially for sparse graph (稀疏图)

### Edge List, EL
- **Edge List** is a collection of edges with both connecting vertices and their weights
- These edges are sorted by increasing weight
- 边列表（Edge List）是表示图的一种简单数据结构，它直接列出了图中所有的边。每条边由一对顶点表示，这对顶点说明了图中的两个顶点之间存在连接。
- 在无权图中，边列表是一个二元组的列表，每个二元组包含两个顶点。例如，边 (u,v) 表示顶点 u 和顶点 v 之间有一条边。
- 在有权图中，边列表通常是一个三元组的列表，每个三元组包含两个顶点以及这两个顶点之间边的权重。例如，边 (u,v,w) 表示顶点 u 和顶点 v 之间有一条权重为 w 的边。

## 6.4 Quiz related
- Connected: all vertices is accessible form any vertex
- Neighbour (adjacent): vertices directly connected to the specific vertex
- Complete Graph: has edge for any pair of vertices
- Tree: 
	- Tree is a **connected graph** with $V$ vertices and $E=V-1$ edges
	- **Acyclic**: does not contain any cycle
	- Has *one unique path* between any pair of vertices
- DAG: No cycle, directed

- Entries of *edge list*: number of edges
- Number of *filled cells* of *adjacency matrix*: $N_{\text{vertices}}^2 - N_{\text{edges}}\times 2$
- Entries of *adjacency list*: each vertex's list contains the direct connected vertices
- Suitable DS for different situation:
	- AM:
		- Dense graph, number of edge approx the square of edges
		- Frequently check existence of edge between two vertices
		- Space complexity $O(n^2$)
	- AL:
		- Sparse graph, number of edges far smaller than the square of edges
		- Frequently check the neighbours of specific vertex
		- Space complexity $\approx 2e$
		- For limited RAM
	- EL:
		- For small number of edges
		- For limited RAM
		- Simple graph structure
		- Space complexity $e$
		- Frequently check all edges (include sorting)

# 7 - DFS & BFS
## 7.1 DFS
- DFS takes one input param: the source vertex `s`
- Trying all options:
	1. If DFS is at a vertex `u` and it has `X` neighbours, it will pick the first neighbour $V_1$ (usually the vertex with the smallest vertex number)
	2. Recursively explore all reachable vertices from vertex $V_1$, and backtrack to vertex $u$
	3. Do the same process (step 1 and 2) for all neighbours, until it finishes exploring the last neighbour $V_x$ and its reachable vertices
- Use an array `status[u]` to record the vertex $u$ is visited or not
- Use another array `p[u]` of size $V$ vertices to remember the parent/predecessor/previous of each vertex $u$ along the DFS traversal path
	- For source vertex $s$, `p[s]` is set to `-1` since the source vertex has no predecessor
- Time complexity is $O(V+E)$
	- Each vertex is only visited once due to the fact that DFS will only recursively explore a vertex $u$ if `status[u] = unvisited`, which takes $O(V)$ time
	- Every time a vertex is visited, all its $k$ neighbours are explored and therefore after all vertices are visited, we have examined all $E$ edges, which takes $O(E)$ time
1. 从一个选定的源节点开始，将其标记为“已访问”，并将其放入栈中。
2. 取栈顶元素为当前节点，探索当前节点的一个未访问的邻居节点。
3. 将新发现的节点标记为“已访问”并放入栈中。
4. 如果当前节点没有未访问的邻居节点，则将它从栈中弹出（回溯）。
	- 这意味着如果重复步骤，则在步骤2选定的节点为该节点的上一个节点
5. 重复步骤2到4，直到栈为空，或者找到目标节点，或者遍历完所有可达的节点。

DFS算法的特点是尽可能深地搜索树的分支，这个特性使得DFS在某些情况下比广度优先搜索（BFS）更加高效，比如在寻找解决方案的路径比较深的问题中。此外，DFS算法的空间复杂度通常较低，因为它不需要存储所有层的节点，只需要维护一个栈的空间即可。
## 7.2 BFS
- BFS take one input param: the source vertex `s`
- BFS start from a source vertex `s` but is uses a queue to order the vistation sequence as *breadth* as possible before going deeper
- BFS also uses a Boolean array of size $V$ vertices to distinguish between two states: visited and unvisited vertices
- Time complexity is $O(V+E)$
	- Each vertex is only visited once as it can only enter the queue once, which takes $O(V)$ time
	- Every time a vertex is dequeued from the queue, all its $k$ neighbours are explored and therefore after all vertices are visited, we examined all $E$ edges, which takes $O(E)$ time
1. **初始化**：首先将根节点放入队列中。
2. **循环遍历**：只要队列不为空，就重复以下步骤：
    - 从队列的前端取出一个节点。
    - 检查它是否为目标。如果找到目标，则搜索结束。
    - 如果它不是目标，则将该节点的所有未访问的邻接点加入队列，并标记这些邻接点为已访问。
3. **访问节点**：对于队列中的每个节点，访问该节点，并检查它是否是目标节点。如果是，则结束搜索并返回结果。如果不是，则将其所有未被访问过的邻居节点加入队列。
4. **标记已访问**：在加入队列的同时，应该将节点标记为已访问，以防止将节点重复加入队列。
5. **重复**：重复步骤2，直到找到目标节点或队列为空，队列为空意味着整个图已经搜索完毕，没有找到目标。

BFS算法的特点在于它提供了最短路径的保证，即第一次找到目标节点时的路径是从根节点到目标节点的最短路径。这个特性使得BFS特别适合解决最短路径或最少步骤的问题。
## 7.3 Applications
### Reachability test
- Call `DFS(s)` or `BFS(s)` to check if `status[t] = visited`
### Print the Traversal Path
- For DFS, print each node when a node is marked as visited
	- i.e., print node once explore to it
- For BFS, print each node when dequeue a node
	- i.e., print node once it is get out form the queue to explore
### Identifying a Connected Component (CC)
- Call `DFS(s)` or `BFS(s)` to enumerate all vertex $v$ that has `status[v] = visited`
### Counting the number of Connected Component
```Python
CC = 0
for all u in V:
	status[u] = unvisited
for all u in V:
	if (status[u] == unvisited):
		CC += 1
		DFS(u) # DFS will visit all nodes connected to this source node
print(CC)
```
## 7.4 Detect Cycle in DFS
- Let array `status[u]` to record three different status:
	- **unvisited**: DFS has not reach the vertex $u$
	- **explored**: DFS is visited the vertex $u$, and there is at least one neighbour for vertex $u$ is not visited
		- i.e., this vertex is still be deepening by DFS
	- **visited**: DFS is visited the vertex $u$ and its all neighbours
- If DFS is now at vertex $x$ and explore edge $x\to y$ and encounter `status[y] = explored`, it means a cycle has been found
## 7.5 Topological Sort for DFS
- When dequeue a node, add this node to the list
- After add all node to the list, reverse the list
![image.png](https://images.wu.engineer/images/2023/11/24/202311241301218.png)

## 7.6 Quiz Related
- Bipartite Graph 二分图
	- 将图分为两个集合，只有集合之间存在边，集合内部没有边
		![image.png](https://images.wu.engineer/images/2023/11/24/202311241315959.png)
- Simple Path 简单路径
	- 即路径上没有重复的节点
- Edges that make up the spanning tree 构成生成树的边
	- 从源点开始DFS/BFS，遍历节点经过的边可以作为构成生成树的边
	- 除了能够构成环的边（即除了到达已经访问过的节点的边）
- Edges that must belongs to every spanning tree
	- 只有单个度的节点的边
- Number of spanning tree of a complete graph with $N$ vertices
	- $T = N^{N-2}$
- Running time for DFS and BFS in different graph structure
	- Connected Graph (not complete): $O(V+E)$
	- Complete Graph: $O(V^2)$
	- Bipartite Graph: $O(V^2)$, worst $O(V+E)
	- DAG: $O(V^2)$, worst $O(V+E)
	- Tree: $O(V)$
	- Acyclic Graph: $O(V+E)$
- Tree
	- 无环
	- 从一个节点到另一个节点只有一条唯一的路径
- Topological Sort 拓扑排序
	- When dequeue a node, add this node to the list
	- After add all node to the list, reverse the list
- Strongly Connected Component
	- 每个顶点都可以通过有向路径到达分量中的任何其他顶点
	- 每个节点只属于一个强连通分量
	- 强连通分量是该节点区域内最大的一个子图
	- 单节点也是强连通分量
# 8 - Single-Source Shortest Paths (SSSP)
- 在此问题中，我们需要在一个有向加权图中找到从特定的顶点到其他所有顶点的最短路径
- SSSP算法中的输入为：
	- 不一定相连的有向加权图G(V,E)
	- 源顶点s
- 输出为：
	- 大小为 V 的数组 D（D 代表 "距离）
		- 最初，如果 u = s，D[u] = 0；否则，D[u] = +∞
		- 当我们找到更好（更短）的路径时，D[u]就会减少
	- 大小为 V 的数组/矢量 p（p 代表 "父数组"/"前置数组"/"前一个数组"）
		- p[u] = 从源节点 s 到 u 的最佳路径上的前置因子
		- p[u] = NULL（未定义，我们可以使用-1 这样的值来表示）
		- 该数组/向量 p 描述了生成的 SSSP 生成树
## relax operation
```Python
def relax(u, v, w_u_v): 
	if D[v] > D[u]+w_u_v: // if the path can be shortened 
		D[v] = D[u]+w_u_v // 'relax' (update) the previous edge to shorter edge
		p[v] = u // remember/update the predecessor
```
- 当我们找到了一个更短的路径时，我们需要进行relax/update 操作，将现有的路径替换(update/relax) 成更短的路径
## Approaches
- 我们可以对不同的图使用不同的算法来解决SSSP问题:
	- Unweighted Graphs 无权图: **BFS** $O(V+E)$
	- Graphs without negative weight 无负权图: **Dijkstra’s Algorithm** $O((V+E) logV)$
	- Graph without negative cycle 无负权循环图: **Modified Dijkstra’s** $O((V+E)logV)$
	- Tree 树: **DFS/BFS** $O(V+E)$
	- Directed Acyclic Graphs (DAG)有向无环图: **Dynamic Programming** $O(V+E)$
### Unweighted Graphs: BFS
在无权重图中，两个节点之间的“最短路径”简单地指的是连接它们的边数最少的路径。BFS 在这种情况下非常合适，因为它按层次（即边数）访问节点，从而能够保证找到的路径是边数最少的。
以下是使用 BFS 解决无权重图的 SSSP 问题的步骤：
1. **初始化**：首先，创建一个队列用于 BFS，并将起点（源点）入队。同时，创建一个数组或字典来存储每个节点到源点的最短距离，初始时除了源点（距离设为0）之外的所有节点距离都设为无穷大或未定义。
2. **进行 BFS**：当队列不为空时，重复以下步骤：
	- 从队列中弹出一个节点。
	- 检查该节点的每个邻居：
		- 如果邻居的最短距离尚未确定（即仍为无穷大或未定义），则更新其最短距离（设置为当前节点的最短距离加1），并将该邻居节点入队。
3. **终止**：当队列为空时，算法结束。此时，存储节点最短距离的数组或字典中的值即为从源点到每个节点的最短路径长度。
```Python
from collections import deque 
def bfs_sssp(graph, start): 
	distances = {vertex: float('infinity') for vertex in graph} 
	distances[start] = 0 
	
	queue = deque([start]) 
	
	while queue: 
		current = queue.popleft() 
		for neighbor in graph[current]: 
			if distances[neighbor] == float('infinity'): 
				distances[neighbor] = distances[current] + 1 
				queue.append(neighbor) 
	
	return distances 
	
# 示例图 
graph = { 
	'A': ['B', 'C'], 
	'B': ['A', 'D', 'E'], 
	'C': ['A', 'F'], 
	'D': ['B'], 
	'E': ['B', 'F'], 
	'F': ['C', 'E'] 
} 
# 计算从节点 'A' 到所有其他节点的最短距离 
print(bfs_sssp(graph, 'A'))
```
### Graphs without negative weight: Dijkstra’s Algorithm
Dijkstra算法适用于有向和无向图，并假定所有边的权重都是非负的。它利用贪心策略，逐步确定从源点到图中所有其他顶点的最短路径。
**Dijkstra算法的基本步骤**:
1. **初始化**：对于图中的每个顶点，将其最短路径估计设置为无穷大，除了源点，其最短路径估计设为0。维护一个优先队列（最小堆），最初包含所有顶点，优先队列按照顶点的最短路径估计进行排序。
2. **处理顶点**：当优先队列非空时，重复以下步骤：
	- 从优先队列中取出最短路径估计最小的顶点（称为当前顶点）。
	- 对于当前顶点的每个相邻顶点，更新其最短路径估计。如果通过当前顶点到达邻居的路径比已知的路径更短，则更新邻居的最短路径估计，并在优先队列中更新其位置。
3. **算法结束**：当优先队列为空时，算法结束。此时，每个顶点的最短路径估计就是从源点到该顶点的最短路径。
```Python
import heapq

def dijkstra(graph, start):
    # 初始化距离表
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    # 初始化优先队列，并放入起点
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        # 如果该顶点的距离已经是最小了，则无需处理
        if current_distance > distances[current_vertex]:
            continue
        # 检查当前顶点的邻居
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            # 更新邻居的距离
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# 示例图
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 5},
    'C': {'A': 4, 'F': 5},
    'D': {'B': 2},
    'E': {'B': 5, 'F': 1},
    'F': {'C': 5, 'E': 1}
}
```
- 在此算法中，每个顶点从优先队列中提取一次$O(logV)$，由于有V个顶点，所以此步骤的运行速度为$O(VlogV)$
- 接下来检查当前顶点的邻居，更新邻居的距离需要用到relax操作，这部分的运行速度为$O(ElogV)$
- 总的运行速度为$O((E+V)logV)$
### Trees: DFS/BFS
由于树没有循环，所以我们可以简单地从源点遍历树，同时累加沿路径的权重，以此计算到每个顶点的最短路径。

由于树是一种没有循环的特殊图，所以在树中，从一个顶点到另一个顶点的路径是唯一的。这意味着无论是使用 DFS 还是 BFS，当你首次到达一个顶点时，你找到的就是从源点到这个顶点的最短（也是唯一的）路径。
**DFS**
```Python
def dfs(tree, node, current_distance, distances, visited):
    visited.add(node)
    distances[node] = current_distance

    for child, weight in tree[node].items():
        if child not in visited:
            dfs(tree, child, current_distance + weight, distances, visited)

def sssp_with_dfs(tree, start):
    distances = {}
    visited = set()
    dfs(tree, start, 0, distances, visited)
    return distances

# 示例树
tree = {
    'A': {'B': 1, 'C': 2},
    'B': {'A': 1, 'D': 4, 'E': 5},
    'C': {'A': 2, 'F': 6},
    'D': {'B': 4},
    'E': {'B': 5},
    'F': {'C': 6}
}

# 计算从节点 'A' 到所有其他节点的最短距离
print(sssp_with_dfs(tree, 'A'))
```
**BFS**
```Python
from collections import deque

def sssp_with_bfs(tree, start):
    distances = {start: 0}
    queue = deque([start])

    while queue:
        node = queue.popleft()
        for child, weight in tree[node].items():
            if child not in distances:
                distances[child] = distances[node] + weight
                queue.append(child)

    return distances

# 使用相同的树结构和起点调用 BFS
print(sssp_with_bfs(tree, 'A'))

```
在这两种方法中，我们都维护了一个 `distances` 字典来记录从源点到每个节点的最短距离。由于树中的路径是唯一的，所以当我们第一次访问每个节点时，计算的距离就是最短距离。DFS 和 BFS 在这种情况下都是有效的，选择哪种方法取决于个人偏好或特定应用场景的需求。
### Directed Acyclic Graphs: Dynamic Programming
动态规划在这类问题中的关键在于利用 DAG 的拓扑排序，确保在计算一个顶点的最短路径时，已经计算了其所有前驱节点的最短路径。

动态规划解决 DAG 的 SSSP 问题的步骤如下：
1. **拓扑排序**：首先对 DAG 进行拓扑排序。拓扑排序是将图中的顶点排成一个线性序列，使得对于图中的每条边 `u -> v`，`u` 在序列中都出现在 `v` 之前。拓扑排序可以通过 DFS 实现。
2. **初始化距离**：将源点到所有顶点的距离初始化为无穷大，除了源点自身的距离为 0。
3. **动态规划更新**：按照拓扑排序的顺序，更新每个顶点的最短路径。对于每个顶点，检查所有进入该顶点的边，并更新该顶点的最短路径。
```Python
from collections import defaultdict, deque

# 拓扑排序的实现
def topological_sort(graph):
    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        order.appendleft(node)

    visited = set()
    order = deque()
    for vertex in graph:
        if vertex not in visited:
            dfs(vertex)
    return order
# 使用 DP 解决 SSSP 问题
def sssp_in_dag(graph, start):
    # 拓扑排序
    topo_order = topological_sort(graph)

    # 初始化距离表
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    # 遍历拓扑排序的顺序，更新距离
    for vertex in topo_order:
        for neighbor, weight in graph[vertex].items():
            distances[neighbor] = min(distances[neighbor], distances[vertex] + weight)

    return distances

# 示例 DAG
dag = {
    'A': {'B': 3, 'C': 6},
    'B': {'C': 4, 'D': 4, 'E': 11},
    'C': {'D': 8, 'G': 11},
    'D': {'E': -4, 'F': 5, 'G': 2},
    'E': {'H': 9},
    'F': {'H': 1},
    'G': {'H': 2},
    'H': {}
}
# 计算从节点 'A' 到所有其他节点的最短距离
print(sssp_in_dag(dag, 'A'))
```
在这个实现中，首先通过 `topological_sort` 函数得到 DAG 的拓扑排序。然后，在 `sssp_in_dag` 函数中使用这个排序来确保在计算每个顶点的最短路径时，其所有前驱节点的最短路径都已经计算过了。这样，我们可以保证动态规划的每一步都是基于正确和最新的信息。
