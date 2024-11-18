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

# -------

tasks = ["Learn Python", "Do exercises", "Drink coffee", "Finish my work"]
tasks
['Learn Python', 'Do exercises', 'Drink coffee', 'Finish my work']
len(tasks)
4
tasks.append("Make food")
tasks
['Learn Python', 'Do exercises', 'Drink coffee', 'Finish my work', 'Make food']
task = "Finish my work"
task
'Finish my work'
task.split()
['Finish', 'my', 'work']
task.split("i")
['F', 'n', 'sh my work']
" ".join(["Finish", "my", "work"])
'Finish my work'
"x".join(["Finish", "my", "work"])
'Finishxmyxwork'
" - ".join(["Finish", "my", "work"])
'Finish - my - work'
sorted("acb")
['a', 'b', 'c']
sorted("ac8b1")
['1', '8', 'a', 'b', 'c']
sorted(tasks)
['Do exercises', 'Drink coffee', 'Finish my work', 'Learn Python', 'Make food']
sorted([4, 1, 5, 8, -5])
[-5, 1, 4, 5, 8]
sorted([4, 1, 5, 8, -5], reverse=True)
[8, 5, 4, 1, -5]
sorted([4, 1, 5, 8, -5], reverse=False)
[-5, 1, 4, 5, 8]
tasks
['Learn Python', 'Do exercises', 'Drink coffee', 'Finish my work', 'Make food']
tasks.pop()
'Make food'
tasks
['Learn Python', 'Do exercises', 'Drink coffee', 'Finish my work']
tasks.pop(1)
'Do exercises'
tasks
['Learn Python', 'Drink coffee', 'Finish my work']
[0] * 10
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[1, 2, 3] + [3, 4]
[1, 2, 3, 3, 4]
tasks
['Learn Python', 'Drink coffee', 'Finish my work']
len(tasks)
3
tasks
['Learn Python', 'Drink coffee', 'Finish my work']
len(tasks)
3
tasks
['Learn Python', 'Drink coffee', 'Finish my work']
sorted(tasks)
['Drink coffee', 'Finish my work', 'Learn Python']
tasks
['Learn Python', 'Drink coffee', 'Finish my work']
tasks.sort()
tasks
['Drink coffee', 'Finish my work', 'Learn Python']
tasks.sort(reverse=True)
tasks
['Learn Python', 'Finish my work', 'Drink coffee']

# ----

task = {"description": "Learn Python"}
task
{'description': 'Learn Python'}
len(task)
1
task["assignee"]
Traceback (most recent call last):
  File "/snap/pycharm-professional/429/plugins/python-ce/helpers/pydev/pydevconsole.py", line 364, in runcode
    coro = func()
           ^^^^^^
  File "<input>", line 1, in <module>
KeyError: 'assignee'
task["description"]
'Learn Python'
task["description"]
'Learn Python'
task.get("description")
'Learn Python'
task.get("assignee")
task.get("assignee") is None
True
task.get("assignee", "no value")
'no value'
task.get("assignee", 0)
0
task.get("assignee", "")
''
task.get("assignee")
task
{'description': 'Learn Python'}
task["description"] = "Learn JavaScript"
task
{'description': 'Learn JavaScript'}
task["priority"]
Traceback (most recent call last):
  File "/snap/pycharm-professional/429/plugins/python-ce/helpers/pydev/pydevconsole.py", line 364, in runcode
    coro = func()
           ^^^^^^
  File "<input>", line 1, in <module>
KeyError: 'priority'
task["priority"] = 2
task
{'description': 'Learn JavaScript', 'priority': 2}
task.get("due_date", task["due_date"])
Traceback (most recent call last):
  File "/snap/pycharm-professional/429/plugins/python-ce/helpers/pydev/pydevconsole.py", line 364, in runcode
    coro = func()
           ^^^^^^
  File "<input>", line 1, in <module>
KeyError: 'due_date'
task["due_date"] = "2024-12-11" if "due_date" in task else None
task
{'description': 'Learn JavaScript', 'priority': 2, 'due_date': None}
task
{'description': 'Learn JavaScript', 'priority': 2, 'due_date': None}
task.pop("due_date")
task
{'description': 'Learn JavaScript', 'priority': 2}
task.pop("description")
'Learn JavaScript'
task
{'priority': 2}
dict().fromkeys(["description", "assignee", "priority", "time_logged", "is_completed", "due_date"])
{'description': None, 'assignee': None, 'priority': None, 'time_logged': None, 'is_completed': None, 'due_date': None}
dict().fromkeys(["description", "assignee", "priority", "tim

tasks_statuses = [True, False, False, True, False]
tasks_statuses
[True, False, False, True, False]
any(tasks_statuses)
True
all(tasks_statuses)
False
any(["a", "b", "c"])
True
bool("a")
True
bool("")
False
any([1, 2, 3])
True
all([1, 0, 2])
False
bool(0)
False


n_of_comments_in_tasks = [2, 0, 6, 0, 0, 9]
n_of_comments_in_tasks
[2, 0, 6, 0, 0, 9]
min(n_of_comments_in_tasks)
0
max(n_of_comments_in_tasks)
9
sum(n_of_comments_in_tasks)
17
sum(n_of_comments_in_tasks) / len(n_of_comments_in_tasks)
2.8333333333333335