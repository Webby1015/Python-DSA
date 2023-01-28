def process_file():
    try:
        f = open("readme.txt")
        x = 1/0
    except FileNotFoundError as e:
        print("inside except")
# finally is used to run code regardless of whether the error was handled or not
    finally:
        print("Cleaning up file")
        f.close()


process_file()

# the above code will return a zerodivision error but it will also return all the contents of finally statement
