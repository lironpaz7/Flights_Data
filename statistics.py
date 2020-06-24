from math import ceil


def sum_function(values):
    """
    This function receives a list of numbers and sum them.
    :param values: list of values
    :return:
    """
    total_sum = 0
    for value in values:
        total_sum += value
    return total_sum


def mean(values):
    """
    This function uses the sum function we made before and divides the result by the length of the list
    to create a mean value.
    :param values: list of values
    :return:
    """
    return (sum_function(values)) / len(values)


def median(values):
    """
    This function takes the list and create a new sorted one. If the list length is even then the formula is:
    X[n/2] + X[n/2 + 1] and divide by 2. Otherwise just take ceil value of X[n/2] and divide by 2.
    :param values: list of values
    :return:
    """
    values = sorted(values)
    length = len(values)
    if length % 2 == 0:
        return (values[int((length - 1) / 2)] + values[int(((length - 1) / 2) + 1)]) / 2
    else:
        return values[ceil((length - 1) / 2)]

