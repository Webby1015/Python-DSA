f = open("E:\\Codes\\Python DSA\\essentials\\fileReadWrite\\text.txt", "r")
f_out = open(
    "E:\\Codes\\Python DSA\\essentials\\fileReadWrite\\text_Wc.txt", "w")
# print(f.read())

#       or

for line in f:
    f_out.write(" word count :" + str(len(line.split(' ')))+" " + line)


f.close()
f_out.close()
