class Node:

    def __init__(self, v):
        self.value = v
        self.next = None
        self.next = None


class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

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
        node = self.head
        while node is not None:
            if node.value == val:
                if node.prev is None:
                    self.head = node.next
                    if self.head is not None:
                        self.head.prev = None
                    if node == self.tail:
                        self.tail = None
                    if not all:
                        return
                else:
                    node.prev.next = node.next
                    if node == self.tail:
                        self.tail = node.prev
                    if node.next is not None:
                        node.next.prev = node.prev
                    if not all:
                        return
                if not all:
                    return
            node = node.next
        if all and self.tail is not None and self.tail.value == val:
            self.tail = self.tail.prev
            if self.tail is not None:
                self.tail.next = None

    def insert(self, afterNode, newNode):
        if newNode is None:
            return
        if afterNode is None and self.head is None:
            newNode.next = self.head
            self.head = newNode
            newNode.prev = None
            if self.head is None:
                self.tail = newNode
            else:
                self.head.prev = newNode
            self.head = newNode
        else:
            node = self.head
            while node is not None:
                if node == afterNode:
                    newNode.next = node.next
                    newNode.prev = node
                    if node == self.tail:
                        self.tail = newNode
                    else:
                        node.next.prev = newNode
                    node.next = newNode
                    return
                node = node.next

    def add_in_head(self, newNode):
        if newNode is None or newNode == "":
            return
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

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
