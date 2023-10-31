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


