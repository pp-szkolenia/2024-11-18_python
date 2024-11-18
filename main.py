from datetime import date


list_of_tasks = [
    {
        'description': "Learn Python",
        "assignee": "Andrzej",
        "priority": 3,
        "due_date": date(2024, 11, 18),
        "is_completed": False,
        # "comments": ["Good luck!", "Thank you"]
        "comments": [{"author": "Andżela", "text": "Good luck!"}, {"author": "Andrzej", "text": "Thank you"}]
    },
]


print(list_of_tasks[0]["comments"][0]["text"])
