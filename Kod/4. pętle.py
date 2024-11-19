for i in range(4):
    print(i)


n_of_users_to_create = 3
users = []

for _ in range(n_of_users_to_create):
    username = input("Enter the username: ")
    password = input("Enter the password: ")

    user = {"username": username, "password": password}

    users.append(user)

print(users)


users = ["Admin", "Andrzej", "Andżela"]


for user in users:
    print(user)


numbers = [1, 2, 3, 4, 5, 6, 7]


for number in numbers:
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")


list_of_users = [
    {"username": "Admin", "password": "admin12345"},
    {"username": "Andrzej", "password": "qwerty"},
    {"username": "Andżela", "password": "ha"},
]


for user in list_of_users:
    print(f"Username: {user['username']}, password: {'*' * len(user['password'])}")

    for character in "hello":
        print(character)
