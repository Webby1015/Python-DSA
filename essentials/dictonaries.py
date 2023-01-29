a = {"tom": 1234, "tim": 3456, "timothy": 5678}
# call value
print(a["tom"])

# delete value
del a["tim"]

# how to print the entire dictionary
print(a)

# how to iterate through the dictionary
for i in a:
    print("key :", i, " value :", a[i])
#       or

for k, v in a.items():
    print("key :", k, " value :", v)
