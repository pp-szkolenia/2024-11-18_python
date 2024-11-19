def my_len(iterable):
    length = 0
    for _ in iterable:
        length += 1
    return length

print(
    my_len([1, 2, 3, 4, 5, 6])
)


def mark_task_as_completed(task):
    if not task["is_completed"]:
        task["is_completed"] = True
    else:
        print("Task already completed")

    return task


print(
    mark_task_as_completed({
        "is_completed": True
    })
)
