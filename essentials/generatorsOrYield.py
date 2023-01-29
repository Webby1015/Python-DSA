# generator is a simple way of creating iterators

def remote_control_next():
    yield "cnn"
    yield "espn"

# yield is similer to return statement the differemce is that
# when we execute return statement it gives the return value and the contents of function are deleted
# but yield saves the contents of function even after function call
# basicly it can be used to have more than one return values


print(remote_control_next())
# this fuction has two values it does not know which one to return so it is giving the address of begining just like a list

print(next(remote_control_next()))
# going up the address we get the first yield statement executed

# print(next(next(remote_control_next()))) we can not use this insted we need to first store the address value

itr = remote_control_next()

print("first yield:", next(itr))
print("Second yield:", next(itr))
#  going up the address we get the second yield statement executed

# an alternative method is
for channels in remote_control_next():
    print(channels)
# this is possible because for also uses the __iter__ method and __ next method
# so if you see remote_control_next() function is kind of stored like a list
#  we use generators because we dont need to use iter and next over and over again
# or stopiteration as it will stop on its own
