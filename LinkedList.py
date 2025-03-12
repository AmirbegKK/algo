class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f'{self.data} -> {self.next}'


class Llist:
    def __init__(self, nodes):
        if nodes is not None:
            node = Node(nodes.pop(0))
            self.head = node
            while nodes:
                node.next = Node(nodes.pop(0))
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append('None')
        return ' -> '.join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        for el in self:
            pass
        el.next = node

    def remove(self, node):
        # while self.head.data == anode.data:
        #     self.head = self.hed.next

        prev = self.head
        cur = self.head.next
        while cur is not None:
            if cur.data == node.data:
                prev.next = cur.next
                cur = cur.next
                return
            else:
                prev = cur
                cur = cur.next

def remove_duplicates_naive(linked_list):
    node_values = set()
    for elem in linked_list:
        if elem.data in node_values:
            linked_list.remove(elem)
        else:
            node_values.add(elem.data)

def remove_duplicates_fast(linked_list: Llist):
    current_node = linked_list.head
    while current_node is not None:
        runner_node = current_node
        while runner_node.next is not None:
            if current_node.data == runner_node.next.data:
                runner_node.next = runner_node.next.next
            else:
                runner_node = runner_node.next

        current_node = current_node.next


def kth_to_last_naive(node: Node, k: int, length: int):
    length += 1
    if node.next is None:
        if k == 0:
            return node
        if k > length:
            return
        return 0

    data  = kth_to_last_naive(node.next, k, length)
    if data is None:
        return
    if not isinstance(data, Node):
        n = data + 1
        if n == k:
            return node
        return n
    return data

class IntWrapper:
    def __init__(self, value):
        self.value = value


def kth_to_last_optimized(node: Node, k: int, index_from_last: IntWrapper):
    if node is None:
        return None

    nd = kth_to_last_optimized(node.next, k, index_from_last)
    index_from_last.value += 1
    if index_from_last.value == k:
        return node
    return nd

def kth_to_last_fast(node: Node, k: int):
    if node is None:
        return

    first_pointer = node
    second_pointer = node
    for _ in range(k):
        second_pointer = second_pointer.next

    while second_pointer is not None:
        first_pointer = first_pointer.next
        second_pointer = second_pointer.next
    return first_pointer

def partition_around_x(linked_list: Llist, x: Node) -> Llist:
    """
    Implementation of algorithm to partition linked list around a value x
    such that all nodes with value less or equal to x come before nodes with value greater than x

    :param linked_list:
    :param x:
    :return:
    """

    node = linked_list.head
    left_part = None
    right_part = None
    while node is not None:
        if node.data <= x.data:
            if left_part is None:
                left_part = Llist([node.data])
            else:
                left_part.add_last(Node(node.data))
        else:
            if right_part is None:
                right_part = Llist([node.data])
            else:
                right_part.add_last(Node(node.data))
        node = node.next

    left_part.add_last(right_part.head)
    return left_part


def _sum_of_digits(linked_list1: Llist, linked_list2: Llist):
    num1 = ''
    num2 = ''

    node1 = linked_list1.head
    node2 = linked_list2.head

    while node1 is not None:
        num1 = node1.data + num1
        node1 = node1.next

    while node2 is not None:
        num2 = node2.data + num2
        node2 = node2.next

    num = str(int(num1) + int(num2))

    return Llist([elem for elem in num[::-1]])

def circular_node(node):
    next_ = node.next
    while node is not None:
        while next_ is not None:
            if next_.data == node.data:
                return next_.data
            next_ = next_.next
        node = node.next



if __name__ == '__main__':
    linked_list_ = Llist(['7','1','6','7','2'])
    # linked_list_2 = Llist(['5','9','2'])
    # linked_list_.remove(Node('3'))
    # print(linked_list_)
    # print(partition_around_x(linked_list_, Node('3')))
    # print(_sum_of_digits(linked_list_, linked_list_2))
    print(circular_node(linked_list_.head))