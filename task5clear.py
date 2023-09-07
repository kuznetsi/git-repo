class Queue:
    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    def enqueue(self, item):
        self.stack_1.append(item)

    def dequeue(self):
        if not self.stack_2:
            while self.stack_1:
                self.stack_2.append(self.stack_1.pop())
        if self.stack_2:
            return self.stack_2.pop()
        return None

    def size(self):
        return len(self.stack_1) + len(self.stack_2)

    def rotate(self, n):
        if n < 0:
            raise ValueError("Need N > 0")
        size = self.size()
        if size <= 1 or n == 0:
            return
        n = n % size
        for _ in range(n):
            item = self.dequeue()
            self.enqueue(item)
