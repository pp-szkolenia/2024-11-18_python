a = float(input("Podaj liczbę a: "))
b = float(input("Podaj liczbę b: "))


if a > b:
    print("a jest większe od b")
elif a < b:
    print("a jest mniejsze od b")
else:
    print("a jest równe b")


int_or_str = "hello!"

if isinstance(int_or_str, int):
    if int_or_str in [4, 6]:
        print("Liczba znajduje się w zbiorze 4,6")
    else:
        print("Liczby nie ma w tym zbiorze")
elif isinstance(int_or_str, str):
    if len(int_or_str) % 2 == 0:
        print("Liczba znaków jest parzysta")
    else:
        print("Liczba znaków jest nieparzysta")
