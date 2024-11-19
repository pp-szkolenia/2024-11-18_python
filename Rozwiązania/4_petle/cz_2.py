i = 0

while i < 10:
    print(i ** 2)
    i += 1


number = input("Podaj liczbę: ")

for digit in number:
    if digit == "0":
        break
    elif int(digit) % 2 != 0:
        print(f"Liczba {digit} - nieparzysta")
    else:
        continue
