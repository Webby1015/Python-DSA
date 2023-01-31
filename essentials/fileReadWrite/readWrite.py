f = open("E:\\Codes\\Python DSA\\essentials\\fileReadWrite\\text.txt", "r")
f_out = open(
    "E:\\Codes\\Python DSA\\essentials\\fileReadWrite\\text_Wc.txt", "w")
# print(f.read())

#       or

for line in f:
    f_out.write(" word count :" + str(len(line.split(' ')))+" " + line)


f.close()
f_out.close()

# if we use "r" mode we can not write so instead we use "r+" to use both
# if we use "w" mode we can not read it so instead we use "w+" to use both

# the difference b/w "r+" and "w+" is "w+" will create a file if it dose not exist wheres "r+" wont


#                                   with statement:

with open("E:\\Codes\\Python DSA\\essentials\\fileReadWrite\\text_Wc.txt", "r") as f:
    print(f.read())
# it works same as before but it closes on its own now
