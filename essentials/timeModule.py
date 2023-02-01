import time


def cal_square(numbers):
    start = time.time()
    result = []
    for number in numbers:
        result.append(number*number)
    end = time.time()
    print("total time taken :" + str((end-start)*1000)+" mil sec")
    return result


def cal_cube(numbers):
    start = time.time()
    result = []
    for number in numbers:
        result.append(number*number*number)
    end = time.time()
    print("total time taken :" + str((end-start)*1000)+" mil sec")
    return result


array = range(1, 100000)
square = cal_square(array)
cube = cal_cube(array)
