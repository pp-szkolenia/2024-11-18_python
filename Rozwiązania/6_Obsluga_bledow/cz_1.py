def modulo(a, b):
    try:
        result = a % b
    except ZeroDivisionError:
        result = None
    else:
        print("Operacja wykonana poprawnie")
    finally:
        return result

print(modulo(12, 0))


def square_number():
    try:
        number = input("Podaj liczbę: ")
        return number ** 2
    except TypeError:
        return None
    else:
        print("Operacje wykonana")


# def get_item_from_list(list_, index):
#     try:
#         return list_[index]
#     except IndexError:
#         return None
#
#
# print(get_item_from_list([1, 2, 3], 22))
#
#
#
