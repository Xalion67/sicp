def sqrt(x):
    """
    Функция вычисляет квадратный корень из числа методом Ньютона
    """
    def sqrt_iter(guess):
        """Рекурсивная реализация метода Ньютона"""
        if (good_enough(guess)):
            return int(guess) if (int(guess) ** 2 - x == 0) else guess
        else:
            return sqrt_iter(improve(guess))

    def improve(guess):
        """
        Нахождение числа-догадки через среднее арифметическое guess
        и частного x и guess
        """
        return average(guess, x / guess)

    def average(guess, quotient_x_on_guess):
        """Нахождение среднего арифметического"""
        return (guess + quotient_x_on_guess) / 2

    def good_enough(guess):
        """Проверка guess на достаточную точность для ответа"""
        return (abs(guess ** 2 - x) < 0.001)

    return sqrt_iter(1.0)
