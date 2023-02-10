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
def create_stack():
    stack = []
    return stack

# IsEmpty check


def check_empty(stack):
    return len(stack) == 0

# push


def push(stack, item):
    stack.append(item)
    return stack

# pop


def pop(stack):
    if(check_empty(stack) != True):
        stack.pop()
    else:
        print('stack empty')
    return stack


stack = create_stack()
push(stack, 1)
push(stack, 2)
push(stack, 3)
print(stack)
pop(stack)
print(stack)
