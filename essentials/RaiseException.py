# you can google python builtin exceptions to get a list of them

try:
    raise MemoryError('memory error')
except MemoryError as e:
    print(e)

# all the exceptions are raised form a generic class exception

try:
    raise Exception("Exception")
except Exception as e:
    print(e)

# All exceptions are an instance of class named exception
