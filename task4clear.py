class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def push(self, value):
        self.stack.append(value)

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None
