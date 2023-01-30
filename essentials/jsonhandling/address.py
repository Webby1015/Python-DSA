import json

book = {}
book["tom"] = {
    'name': 'tom',
    'address': '21 RedStreet, NewYork',
    'phone': 9039383747
}

book['bob'] = {
    'name': 'bob',
    'address': '52 Greenstreet, NY',
    'phone': 783456297
}
# a = json.dump(book)
s = json.dumps(book)

print(s)
with open("E:\Codes\Python DSA\essentials\jsonhandling\json.txt", "w") as f:
    f.write(s)
