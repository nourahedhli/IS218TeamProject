from Calculator.Addition import addition
from Calculator.Division import division
from Statistics.randomData import random_code


def mean(data):
    num_values = len(data)
    total = 0
    for num in data:
        total = addition(total, num)
    return division(num_values, total)


def foo(l):
    try:
        l[0]
        return l
    except IndexError:
        return None