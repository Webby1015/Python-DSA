class RemoteControl():
    def __init_(self):
        self.channels = ["HBO", "CNN", "ABC", "ESPN"]
        self.index = -1
# here by using __iter__ on self we get the beginning address of that instance

    def __iter__(self):
        return self
# by defining __next__ we change the normal use of __next__ to whatever we defined

    def __next__(self):
        # self.index += 1
        if self.index == len(self.channels):
            raise StopIteration
        return self.channels[self.index]


# by writing __int__ , __next__ like this we are calling these methods in our class
r = RemoteControl()
itr = iter(r)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
