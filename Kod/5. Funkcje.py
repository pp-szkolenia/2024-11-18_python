def add(a, b):
    return a + b


def add_wrapper(a, b):
    c = add(a, b)
    return c


add_wrapper(2, 3)

