class Circularqueue():
    def __init__(self, k):
        self.queue = [None] * k
        self.head = self.tail = -1

    def enqueue(self, item):
        if ((self.tail + 1) % self.k == self.head):
            print("Queue is full")
        elif (self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = item
        else:
            self.tail == (self.tail + 1) % self.k
            self.queue[self.tail] = data

    def dequeue(self):
        if(self.head == -1):
            print("queue is empty")
        elif(self.head == self.tail):
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.k
            return temp

        def printCqueue(self):
            if(self.head == -1):
                print("Empty queue")
            elif (self.tail >= self.head):
                for i in range(self.head, self.tail+1):
                    print(self.queue[i], end=" ")
                print()
            else:
                for i in range(self.head, self.k):
                    print(self.queue[i], end=" ")
                for i in range(0, self.tail+1):
                    print(self.queue[i], end=" ")
                print()
