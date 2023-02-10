# it folows LIFO i.e Last in first out
# visualize a stack of card in a cuboidal box wit only one opening
# the first card you place will be at the bottom always
# to remove the first card you need to remove the last cards first
# hence the name LIFO

# operations of stack
# Push, Pop, IsEmpty. Isfull, Peek
# we will not code Isfull because lists in python are dynamic so they can expand
# we will not code peek because it's just the card thats on the top

# creating a stack
class stack:
    def __init__(self):
        self.stack = []

    def check_empty(self):
        return len(self.stack == 0)

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if(len(self.stack) == 0):
            return None
        self.stack.pop()

    def display(self):
        print(self.stack)


s = stack()
s.push(1)
s.push(2)
s.display()
s.pop()
s.display()
