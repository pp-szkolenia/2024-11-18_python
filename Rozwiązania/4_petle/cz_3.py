tasks = [
 {"description": "Learn Python", "comments": ["Good luck!", "Don't forget"]},
 {"description": "Finish my work", "comments": ["Finally", "Do it today"]}
]

for task in tasks:
    print(f"Task: {task['description']}")
    for comment in task['comments']:
        print(comment)
    print()
