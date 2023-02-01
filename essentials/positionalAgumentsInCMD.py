# these are used to pass arguments while running the
# python file in command line to give arguments
# there are two types of arguments positional and optional

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("n1", help="Enter first number")
    parser.add_argument("n2", help="Enter Second Argument")
    parser.add_argument("oper", help="Enter operation to be performed")

    args = parser.parse_args()

    print(args.n1)
    print(args.n2)
    print(args.oper)
#                               OUTPUT

# E:\Codes\Python DSA\essentials> python .\positionalAgumentsInCMD.py 2 4 add
# 2
# 4
# add

# this is how you'll pass a positional argument in cmd
# each argument comes one after another as they are defined in the program
# to find out the argument name and help statement you add -h or --help at he end of file name
# like this


# PS E:\Codes\Python DSA\essentials> python .\positionalAgumentsInCMD.py -h
# usage: positionalAgumentsInCMD.py [-h] n1 n2 oper

# positional arguments:
#   n1          Enter first number
#   n2          Enter Second Argument
#   oper        Enter operation to be performed

# optional arguments:
#   -h, --help  show this help message and exit


# you must supply all the arguments or the program will throw an error
