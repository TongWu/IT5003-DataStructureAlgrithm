# Graph

- **Connected**: all vertices is accessible form any vertex
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

# BFS & DFS

-   DFS:
    1. 从一个选定的源节点开始，将其标记为“已访问”，并将其放入栈中。
    2. 取栈顶元素为当前节点，探索当前节点的一个未访问的邻居节点。
    3. 将新发现的节点标记为“已访问”并放入栈中。
    4. 如果当前节点没有未访问的邻居节点，则将它从栈中弹出（回溯）。
      - 这意味着如果重复步骤，则在步骤2选定的节点为该节点的上一个节点
    5. 重复步骤2到4，直到栈为空，或者找到目标节点，或者遍历完所有可达的节点。
-   BFS:
    1. **初始化**：首先将根节点放入队列中。
    2. **循环遍历**：只要队列不为空，就重复以下步骤：
        - 从队列的前端取出一个节点。
        - 检查它是否为目标。如果找到目标，则搜索结束。
        - 如果它不是目标，则将该节点的所有未访问的邻接点加入队列，并标记这些邻接点为已访问。
    3. **访问节点**：对于队列中的每个节点，访问该节点，并检查它是否是目标节点。如果是，则结束搜索并返回结果。如果不是，则将其所有未被访问过的邻居节点加入队列。
    4. **标记已访问**：在加入队列的同时，应该将节点标记为已访问，以防止将节点重复加入队列。
    5. **重复**：重复步骤2，直到找到目标节点或队列为空，队列为空意味着整个图已经搜索完毕，没有找到目标。
-   Print the traversal path
    -   For DFS, print each node when a node is marked as visited
        -   i.e., print node once explore to it
    -   For BFS, print each node when dequeue a node
        -   i.e., print node once it is get out form the queue to explore

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
