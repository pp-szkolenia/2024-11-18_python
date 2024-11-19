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


task = {
    "description": "Learn Python",
    "assignee": "Andrzej",
    "due_date": None,
    "priority": 2,
    "is_completed": False,
    "tags": ["python", "dev"],
    "comments": []
}


for param in task:
    print(param)


for key, value in task.items():
    print(f"Key: {key}, value: {value}")

i = 10

while i > 0:
    print(i)
    i -= 1


list_of_tasks = ["Learn Python", "Do exercises",
                 "Drink coffee", "Finish my work"]

while list_of_tasks:
    # Complete the last task
    list_of_tasks.pop()

    print("To do:", list_of_tasks, "\n")

i = 10

while True:
    print(i)
    i -= 1

    if i < 0:
        break

for number in [1, 2, 3, 4, 5, 6, 7, 8]:
    if number % 2 == 0:
        continue

    print(number)


list_of_tasks = [
    {"description": "Learn Python", "priority": 3},
    {"description": "Do exercises", "priority": 2},
    {"description": "Drink coffee", "priority": 1},
    {"description": "Finish my work", "priority": 2}
]

for task in list_of_tasks:
    if task["priority"] < 2:
        continue

    print(f"Doing: {task['description']}")


for i in range(1, 4):
    for j in range(1, 6):
        print(f"{i} * {j} = {i * j}")

    print("\n")


users = ["Admin", "Andrzej", "Andżela"]
tasks = ["Learn Python", "Do exercises", "Drink coffee"]

for user in users:
    for task in tasks:
        print(f"{user} does: '{task}'")

    print("\n")



list_of_tasks = [
    {"description": "Learn Python", "is_completed": True, "priority": 3},
    {"description": "Do exercises", "is_completed": False, "priority": 2},
    {"description": "Drink coffee", "is_completed": True, "priority": 1},
    {"description": "Finish my work", "is_completed": False, "priority": 2}
]

# result = []
# for task in list_of_tasks:
#     result.append(task["is_completed"])
#
# print(result)

result = [task["is_completed"]
          for task in list_of_tasks]
print(result)

print(
    [{task['description']: task["is_completed"]} for task in list_of_tasks]
)


result = []
for task in list_of_tasks:
    if not task["is_completed"]:
        result.append(task["description"])

# print(result)

result = [task["description"]
          for task in list_of_tasks
          if task["is_completed"]]
print(result)


result = []

for task in list_of_tasks:
    if not task["is_completed"]:
        result.append(task["description"])
    else:
        result.append("Done")

result = [task['description']
          if not task["is_completed"] else "Done"
          for task in list_of_tasks]
print(result)