class Circularqueue():
    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1

    def dequeue(self):
        if self.head == self.tail:
            print("queue empty")
