def sqrt_Newton(x):
    def method_Newton(guess):
        if (good_enough(guess)):
            return int(guess) if (int(guess) ** 2 - x == 0) else guess
        else:
            return method_Newton(improve(guess))

    def improve(guess):
        return average(guess, x / guess)

    def average(guess, quotient_x_on_guess):
        return (guess + quotient_x_on_guess) / 2

    def good_enough(guess):
        return (abs(guess ** 2 - x) < 0.001)

    return method_Newton(1.0)
