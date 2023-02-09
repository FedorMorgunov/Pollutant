# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification

def sumvalues(values):
    """Your documentation goes here"""

    res = 0

    for i in values:
        try:
            res += i
        except TypeError:
            raise Exception('Non-numerical values are present in the list')

    return res

    ## Your code goes here


def maxvalue(values):
    """Your documentation goes here"""

    index = 0

    for i in range(len(values)):
        try:
            if values[i] > values[index]:
                index = i
        except TypeError:
            raise Exception('Non-numerical values are present in the list')
    return index

    ## Your code goes here


def minvalue(values):
    """Your documentation goes here"""

    index = 0

    for i in range(len(values)):
        try:
            if values[i] < values[index]:
                index = i
        except TypeError:
            raise Exception('Non-numerical values are present in the list')
    return index

    ## Your code goes here


def meannvalue(values):
    """Your documentation goes here"""

    return sumvalues(values)/len(values)

    ## Your code goes here


def countvalue(values, x):
    """Your documentation goes here"""

    counter = 0

    for i in values:
        if i == x:
            counter += 1

    return counter

    ## Your code goes here
