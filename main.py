# raise TypeError("Błąd związany z typem")


assert 4 == 4, "Liczby nie są równe"

# print("Asercja poprawna")


def add(a, b):
    return a + b + 1


def test_add():
    assert add(1, 2) == 3, "..."


test_add()
