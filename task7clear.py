class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class OrderedList:
    def __init__(self, asc=True):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def set_asc(self, asc):
        self.__ascending = asc

    def compare(self, v1, v2):
        if v1 < v2:
            return -1
        elif v1 == v2:
            return 0
        else:
            return 1

    def add(self, value):
        if not isinstance(value, (int, float)):
            return
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            current = self.head
            prev = None
            while current is not None:
                comparison_result = self.compare(current.value, value)
                if (self.__ascending and comparison_result > 0) or (not self.__ascending and comparison_result < 0):
                    break
                prev = current
                current = current.next
            if current is None:
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node
            else:
                if prev is None:
                    new_node.next = self.head
                    self.head.prev = new_node
                    self.head = new_node
                else:
                    prev.next = new_node
                    new_node.prev = prev
                    new_node.next = current
                    current.prev = new_node

    def find(self, val):
        current = self.head
        while current is not None:
            comparison_result = self.compare(current.value, val)
            if comparison_result == 0:
                return current
            elif (self.__ascending and comparison_result > 0) or (not self.__ascending and comparison_result < 0):
                break
            current = current.next
        return None

    def delete(self, val):
        current = self.head
        while current is not None:
            comparison_result = self.compare(current.value, val)
            if comparison_result == 0:
                if current.prev is None:
                    self.head = current.next
                    if self.head is not None:
                        self.head.prev = None
                else:
                    current.prev.next = current.next
                if current.next is not None:
                    current.next.prev = current.prev
                if current == self.tail:
                    self.tail = current.prev
                return
            elif (self.__ascending and comparison_result > 0) or (not self.__ascending and comparison_result < 0):
                break
            current = current.next

    def clean(self):
        self.__ascending = True
        self.head = None
        self.tail = None

    def len(self):
        length = 0
        current = self.head
        while current is not None:
            length += 1
            current = current.next
        return length

    def get_all(self):
        result = []
        current = self.head
        while current is not None:
            result.append(current.value)
            current = current.next
        return result


class OrderedStringList(OrderedList):
    def __init__(self, asc=True):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        if not isinstance(v1, str) or not isinstance(v2, str):
            return
        stripped_v1 = v1.strip()
        stripped_v2 = v2.strip()
        if self.__ascending:
            return 1 if stripped_v1 > stripped_v2 else (-1 if stripped_v1 < stripped_v2 else 0)
        else:
            return 1 if stripped_v1 < stripped_v2 else (-1 if stripped_v1 > stripped_v2 else 0)
