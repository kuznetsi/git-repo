class Node:

    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:

    def __init__(self):
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
        while node is not None:
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
        if val is None or val == "":
            return
        if self.head is None:
            return
        if self.head.value == val:
            if self.head == self.tail:
                self.head = None
                self.tail = None
                return
            else:
                self.head = self.head.next
                if not all:
                    return
        prev_node = self.head
        current_node = prev_node.next
        while current_node is not None:
            if current_node.value == val:
                prev_node.next = current_node.next
                if current_node == self.tail:
                    self.tail = prev_node
                if not all:
                    return
            else:
                prev_node = current_node
            current_node = current_node.next
        if all and self.tail is not None and self.tail.value == val:
            prev_node.next = None
            self.tail = prev_node

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        length = 0
        if self.head is None:
            return length
        else:
            node = self.head
            while node is not None:
                length += 1
                node = node.next
            return length

    def insert(self, afterNode, newNode):
        if newNode is None:
            return
        if afterNode is None:
            newNode.next = self.head
            self.head = newNode
            if self.tail is None:
                self.tail = newNode
        else:
            node = self.head
            available_afterNode = False
            while node is not None:
                if node == afterNode:
                    available_afterNode = True
                    newNode.next = node.next
                    node.next = newNode
                    if node == self.tail:
                        self.tail = newNode
                    break
                node = node.next
            if not available_afterNode:
                return
