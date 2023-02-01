# these are used to pass arguments while running the
# python file in command line to give arguments
# there are two types of arguments positional and optional

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--n1", help="Enter first number")
    parser.add_argument("--n2", help="Enter Second Argument")
    parser.add_argument("--oper", help="Enter operation to be performed")

    args = parser.parse_args()

    print(args.n1)
    print(args.n2)
    print(args.oper)

# the main difference in code is you just write --n1 for a variable instead of n1

#                                 output

# python .\optionalArgumentsinCMD.py --n1 4 --n2 5 --oper add
# 4
# 5
# add

# if you miss an argument it shows the proper syntax to write it
# the arguments does not have to be in the same sequence as declared
