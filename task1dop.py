class Node:

    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def __len__(self):
        length = 0
        node = self.head

        while node is not None:
            length += 1
            node = node.next

        return length


def sum_linked_lists(list1, list2):
        if len(list1) != len(list2):
            return

        result_list = LinkedList()
        node1 = list1.head
        node2 = list2.head

        while node1 is not None:
            value_sum = node1.value + node2.value
            result_list.add_in_tail(Node(value_sum))

            node1 = node1.next
            node2 = node2.next

        return result_list


list1 = LinkedList()
list1.add_in_tail(Node(1))
list1.add_in_tail(Node(2))
list1.add_in_tail(Node(3))

list2 = LinkedList()
list2.add_in_tail(Node(4))
list2.add_in_tail(Node(5))
list2.add_in_tail(Node(6))

result = sum_linked_lists(list1, list2)
result.print_all_nodes()


