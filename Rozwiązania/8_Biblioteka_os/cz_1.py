import os

print(os.getcwd())
print(os.listdir())
print(os.listdir())

path = os.path.join(os.getcwd(), "../6_Obsluga_bledow")

for item in os.listdir(path):
    if os.path.isfile(os.path.join(path, item)):
        print(f"Item: {item} jest plikiem")
    elif os.path.isdir(os.path.join(path, item)):
        print(f"Item: {item} jest folderem")
    else:
        print("Nie jest to plik ani folder")
