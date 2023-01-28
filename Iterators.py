a = ["Hey", "Bro", "How are", "You"]
for i in a:
    print(i)

print(dir(a))

# dir will show all  the methods that can be used on a
# one of those methods is __iter__
itr = iter(a)
# iter makes a poiner for the beginning of the list
print("first item: ", next(itr))
print("Second item: ", next(itr))
print("Third itme: ", next(itr))
print()
# next sends it to the next items address
reverse_itr = reversed(a)

# reversed will give the address of last item and keep all the succedding items in reverse order after that

print("Last item: ", next(reverse_itr))
print("Second last item: ", next(reverse_itr))
print("Third last itme: ", next(reverse_itr))
