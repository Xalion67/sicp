def sum_of_squares_of_top_two(a, b, c):
    if a < b and a < c:
        return b ** 2 + c ** 2
    elif b < a and b < c:
        return a ** 2 + c ** 2
    else:
        return a ** 2 + b ** 2
