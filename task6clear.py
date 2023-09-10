class Deque:
    def __init__(self):
        self.items = []

    def addFront(self, item):
        self.items.insert(0, item)

    def addTail(self, item):
        self.items.append(item)

    def removeFront(self):
        if not self.items:
            return
        return self.items.pop(0)

    def removeTail(self):
        if not self.items:
            return
        return self.items.pop()

    def size(self):
        return len(self.items)

def palindrom(input_string):
    input_string = input_string.lower().replace(" ", "")
    char_deque = Deque()
    for char in input_string:
        if char.isalpha():
            char_deque.addTail(char)
    while char_deque.size() > 1:
        if char_deque.removeFront() != char_deque.removeTail():
            return False
    return True
