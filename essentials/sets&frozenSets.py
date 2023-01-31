#                   sets

basket = {"orange", "apple", "apple", "orange"}
print(basket)
type(basket)

#           or
a = set()
a.add(3)
a.add(3)
a.add(5)
print(a)
# if we a={} it will be declared as a dictionary as long is there is no content in it

#                   frozen sets
# in a frozenset you can not change the elements
# can not add can not delete
n = [1, 2, 3, 4, 5, 5, 4, 3]
n = frozenset(n)
print(n)

#  Set theory using sets in python

x = {"b", "c", "a"}
y = {"a", "h", "g"}
print(x | y)

# x|y is same as x union y
# x&y is same as x intersection y
