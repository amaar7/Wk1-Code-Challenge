def exactly_two_positive(a, b, c):

    # Count the number of positive integers among a, b, c
    count_positive = sum(x > 0 for x in (a, b, c))

    # Return True if exactly two numbers are positive, otherwise False
    return count_positive == 2
