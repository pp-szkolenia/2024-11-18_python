def add_comment(task, comment):
    task["comments"].append(comment)


task = {"is_completed": True,
        "comments": []}

comment = {"author": "...", "text": "..."}

add_comment(task, comment)
print(task)
