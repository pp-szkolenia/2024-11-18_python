list_of_tasks = [
    {"description": "Learn Python", "is_completed": True, "priority": 3},
    {"description": "Do exercises", "is_completed": False, "priority": 2},
    {"description": "Drink coffee", "is_completed": False, "priority": 1},
    {"description": "Finish my work", "is_completed": True, "priority": 2}
]

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
