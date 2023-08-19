class Node:

    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:

    def init(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head

        while node is not None:
            if node.value == val:
                return node
            node = node.next

        return None

    def find_all(self, val):
        found_nodes = []
        node = self.head
        while node is not None:
            if node.value == val:
                found_nodes.append(node)
            node = node.next

        return found_nodes

    def delete(self, val, all=False):
        if self.head is None:
            return

        if self.head.value == val:
            self.head = self.head.next
            if not all:
                return

        prev_node = self.head
        current_node = prev_node.next

        while current_node is not None:
            if current_node.value == val:
                prev_node.next = current_node.next
                if not all:
                    return
            else:
                prev_node = current_node

            current_node = current_node.next

    def clean(self):
        self.head = None
        self.tail = None

    def __len__(self):
        length = 0
        node = self.head

        while node is not None:
            length += 1
            node = node.next

        return length

    def insert(self, afterNode, newNode):
        if afterNode is None:
            newNode.next = self.head
            self.head = newNode
            if self.tail is None:
                self.tail = newNode
            return

        node = self.head
        while node is not None:
            if node == afterNode:
                newNode.next = node.next
                node.next = newNode
                if node == self.tail:
                    self.tail = newNode
                return

            node = node.next
