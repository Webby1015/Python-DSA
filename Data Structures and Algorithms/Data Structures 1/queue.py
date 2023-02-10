# this follows FIFO i.e first in first out
# a queue is like a line waiting at the canteen the first one gets served first
# hence the name FIFO

# operations of Queue
# Enqueue, Dequeue, IsEmpty, IsFull, Peek
# I am not going to code IsFull and Peek because Lists are dynamic and Peek is just the element at the end

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def deque(self):
        if(len(self.queue) == 0):
            return None
        return self.queue.pop(0)

    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.display()
q.deque()
q.display()
print(q.size())
