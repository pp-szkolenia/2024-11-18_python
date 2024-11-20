def modulo(a, b):
    try:
        result = a % b
    except ZeroDivisionError:
        result = None
    else:
        print("Operacja wykonana poprawnie")
    finally:
        return result