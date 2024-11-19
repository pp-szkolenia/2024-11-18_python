numbers = list(range(2, 31))

print(
    [number * 3
     for number in numbers
     if number % 4 == 0]
)

task_comments = [["Comment_1_1", "Comment_1_2"],
 ["Comment_2_1"],
 ["Comment_3_1", "Comment_3_2", "Comment_3_3"]]

print([len(comments) for comments in task_comments])
