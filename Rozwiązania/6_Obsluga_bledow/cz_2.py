def modulo(a, b):
    return a % b + 1


result = modulo(14, 3)

# assert result == 2

if result != 2:
    raise ValueError("Błędny wynik")
