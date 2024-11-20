def modulo(a, b):
    try:
        return a % b
    except ZeroDivisionError:
        return None

print(modulo(2, 0))


def square_number():
    try:
        number = input("Podaj liczbę: ")
        return number ** 2
    except TypeError:
        return None


def get_item_from_list(list_, index):
    try:
        return list_[index]
    except IndexError:
        return None


print(get_item_from_list([1, 2, 3], 22))



