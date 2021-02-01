def square_of_sum(count):
    sum = 0
    i = 1
    while i <= count:
        sum += i
        i += 1
    sum **= 2
    return sum


def sum_of_squares(count):
    sum = 0
    i = 1
    while i <= count:
        sum += i ** 2
        i += 1
    return sum


def difference(count):
    return square_of_sum(count) - sum_of_squares(count) 

def differenceOpti(count):
    sum_square_of_sum = 0
    sum_sum_of_squares = 0
    i = 1
    while i <= count:
        sum_square_of_sum += i
        sum_sum_of_squares += i ** 2
        i += 1
    sum_square_of_sum **= 2
    return sum_square_of_sum - sum_sum_of_squares