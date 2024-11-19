1 >=0
True
4 == 5
False
4 != 5
True
5 > 3 > 1
True
3 in [1, 2, 3, 4]
True
3 in [1, 2, 4]
False
3 not in [1, 2, 4]
True
not False 
True
not True
False
3 not in [1, 2, 4]
True
not 3 in [1, 2, 4]
True
my_list = [1, 2, 4]
3 in my_list
False
"a" in "hello"
False
"el" in "hello"
True
variable = None
variable
variable == None
True
variable is None
True
variable = False 
variable == False 
True
variable is False
True
not variable
True
variable is None
False
variable is not None
True


true = True
false = False

print(true and true)
print(true and false)
print(false and true)
print(false and false)

print(true or true)
print(true or false)
print(false or true)
print(false or false)


is_task_completed = True

if is_task_completed:
    print("The task is completed")

task_1_priority = 3
task_2_priority = 2

if task_1_priority < task_2_priority:
    print("Task 1 is more important")
