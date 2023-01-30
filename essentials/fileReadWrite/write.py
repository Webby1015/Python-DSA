f = open("E:\\Codes\\Python DSA\\essentials\\fileReadWrite\\text.txt", "w")
f.write("I love python")
f.close()
# while writing path it's same as traditoinal path just use \\ instead of \
# "w" overwrites the content on file
# "a" will append to existing file
f = open("E:\\Codes\\Python DSA\\essentials\\fileReadWrite\\text.txt", "a")
f.write("\nI love javaScript")
f.close()
