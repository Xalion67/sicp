def p():
    return p()


def test(x, y):
    if x == 0:
        return 0
    return y


test(0, p())
