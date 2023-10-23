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
> 2. 然后再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
> 3. 以此类推，直到所有元素均排序完毕。

#### Steps:

1. Found the minimum(maximum) element from the unsorted part, store it 

#### Time Complexity



#### Code



### 1.1.3 Merge Sort

#### Steps:



#### Time Complexity



#### Code



### 1.1.4 Quick Sort

#### Steps:



#### Time Complexity



#### Code



### 1.1.5 Random Quick Sort

#### Steps:



#### Time Complexity



#### Code



## 1.2 Non Comparison-based Sorting Algorithms

### 1.2.1 Counting Sort

#### Steps:



#### Time Complexity



#### Code



### 1.2.2 Radix Sort

#### Steps:



#### Time Complexity



#### Code

