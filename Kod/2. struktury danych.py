task_1 = "Learn Python"
task_2 = "Do exercises"
task_3 = "Drink coffee"
task_4 = "Finish my work"


tasks = [task_1, task_2, task_3, task_4]
tasks[2] = "Drink tea"
print(tasks)

mixed_list = [1, "a", 1.234, None, False, [1, 2, 3]]
print(mixed_list[-1][1])

empty_list = []

# ----

possible_priorities = (1, 2, 3)

print(type(possible_priorities))

mixed_tuple = (1, "hello", True, (1, 2, 3), [3, 4])
print(mixed_tuple[1])

empty_tuple = ()

# ----

task = {
        "description": "Learn Python",
        "assignee": "Andrzej",
        "priority": 1,
        "time_logged": 6.25,
        "is_completed": False,
        "due_date": None
    }

print(task["priority"])
task["priority"] = 2
print(task["priority"])

# ---

available_categories = {"dev", "work", "work", "home"}

print(available_categories)

list_with_duplicates = ["dev", "dev", "work"]
print(list(set(list_with_duplicates)))
