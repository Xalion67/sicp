def sqrt(x):
    def sqrt_iter(guess):
        if (good_enough(guess)):
            return int(guess) if (int(guess) ** 2 - x == 0) else guess
        else:
            return sqrt_iter(improve(guess))

    def improve(guess):
        return average(guess, x / guess)

    def average(guess, quotient_x_on_guess):
        return (guess + quotient_x_on_guess) / 2

    def good_enough(guess):
        return (abs(guess ** 2 - x) < 0.001)

    return sqrt_iter(1.0)
