def validate_comment(comment):
    if not isinstance(comment, dict):
        return False

    if not all(param in comment for param in ["author", "text"]):
        return False

    if not (isinstance(comment["text"], str) and
            isinstance(comment["author"], str)):
        return False

    return True


def add_comment(task, comment):
    if validate_comment(comment):
        task["comments"].append(comment)
    else:
        print("ERROR, niepoprawny komentarz")


task = {"is_completed": True,
        "comments": []}

comment = ["hello"]  # {"author": "...", "text!": "..."}

add_comment(task, comment)
print(task)
