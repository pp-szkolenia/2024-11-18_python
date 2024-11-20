try:
    x = 2 / 0
except ZeroDivisionError:
    print("Nastąpił błąd")
finally:
    print("To się wykona zawsze")
