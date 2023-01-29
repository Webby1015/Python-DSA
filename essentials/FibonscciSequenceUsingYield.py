def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b
# the above fuction is making a list like arrangement of all the fibonacci no. when called
# refer to generatorsOrYield.py in this repo


for n in fib():
    if n > 100:
        break
    print(n)
# processing of new statement is only done when if condition is not satisfied
# so fib is not making an infinite long list
