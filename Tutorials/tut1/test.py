class ListNode:
    def __init__(self, name):
        self.name = name
        self.prev = None
        self.next = None


def main():
    # 读取输入值
    n, q = map(int, input().split())

    # 存储舞者和他们的伴侣
    dancers = {}  # 字典，用于快速查找舞者的节点
    partners = {}  # 字典，用于存储舞者与其伴侣的配对
    head = None
    current = None

    # 读取舞者并创建双向链表
    for _ in range(n):
        dancer1, dancer2 = input().split()
        node1 = ListNode(dancer1)
        node2 = ListNode(dancer2)

        # 设置伴侣信息
        partners[dancer1] = dancer2
        partners[dancer2] = dancer1

        # 构建双向链表
        if head is None:
            head = node1
            current = head
        else:
            current.next = node1
            node1.prev = current
            current = node1

        current.next = node2
        node2.prev = current
        current = node2

        # 加入字典以便查找
        dancers[dancer1] = node1
        dancers[dancer2] = node2

    # 确定链表的最后一个节点
    tail = current

    # 处理每个指令
    instructions = input().strip()
    current = head  # 当前持有麦克风的舞者
    for instruction in instructions:
        if instruction == 'F':
            current = current.next
        elif instruction == 'B':
            current = current.prev
        elif instruction == 'R':
            if current != tail:
                # 从链表中移除当前节点并将其移至末尾
                prev_node = current.prev
                next_node = current.next
                if prev_node:
                    prev_node.next = next_node
                if next_node:
                    next_node.prev = prev_node

                tail.next = current
                current.prev = tail
                current.next = None
                tail = current

                current = next_node  # 麦克风传给下一个舞者
            else:
                current = head  # 如果已经在末尾，则传给头部舞者
        elif instruction == 'C':
            if current != tail:
                # 找到舞伴，执行类似的操作
                partner_name = partners[current.name]
                partner_node = dancers[partner_name]

                # 移动逻辑与 'R' 类似，但移动到 partner_node 后面
                # ...（这部分需要实现逻辑，确保更新所有相关节点的 prev 和 next 指针）
            else:
                current = head  # 如果已经在末尾，则传给头部舞者
        elif instruction == 'P':
            print(current.name)  # 打印名字

    print()  # 打印一个空行作为输出的一部分

    # 输出最终的队列状态
    current = head
    while current:
        print(current.name)
        current = current.next


# 运行主函数
if __name__ == "__main__":
    main()
