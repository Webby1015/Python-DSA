import json
f = open("E:\Codes\Python DSA\essentials\jsonhandling\json.txt", "r")
s = f.read()
print(s)

book1 = json.loads(s)
print(book1)
print(type(book1))
print(book1['bob']['phone'])
