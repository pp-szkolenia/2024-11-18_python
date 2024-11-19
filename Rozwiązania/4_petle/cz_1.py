number = input("Podaj liczbę: ")

for digit in number:
    if int(digit) % 2 == 0:
        print(f"Liczba {digit} - parzysta")
    else:
        print(f"Liczba {digit} - nieparzysta")



reference_task = {"id": 1, "priority": 2}

list_of_tasks = [{"id": 2, "priority": 2},
                 {"id": 3, "priority": 1},
                 {"id": 4, "priority": 3}]

for task in list_of_tasks:
    if reference_task["priority"] > task["priority"]:
        print(f"Priorytet taska {reference_task['id']} jest większy niż priorytet taska {task['id']}")
    elif reference_task["priority"] < task["priority"]:
        print(f"Priorytet taska {reference_task['id']} jest mniejszy niż priorytet taska {task['id']}")
    else:
        print(f"Priorytet taska {reference_task['id']} jest równy priorytetowi taska {task['id']}")

