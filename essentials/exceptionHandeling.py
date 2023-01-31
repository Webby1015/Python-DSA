x = input("enter number 1: ")
y = input("enter number 2: ")

try:
    z = int(x)/int(y)
except Exception as e:
    print("Error :", e)
    z = None
print("Solution is :", z)

# the above code gives the solution
# if an error is encountered it makes the solution = None
# this is used to avoid crashes
# Exception has all the general errors but not any specific errors
# instead of Exception we can write the exception name
# use exception to find out exception name or google it
