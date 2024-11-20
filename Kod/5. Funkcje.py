def add(a, b):
    return a + b


def add_wrapper(a, b):
    c = add(a, b)
    return c


add_wrapper(2, 3)


def subtract(a, b=1):
    return a - b


print(
    subtract(20, 5)
)

def create_task(description, tags=[]):
    task = {"description": description, "tags": tags}
    return task


task = create_task("opis zadania")
print(task)


def function(x=None):
    if x is None:
        x = []

    x.append(1)
    print(x)


function()
function()
function()
function()

# ---


def add(a: int, b: int):
    """
    This function adds two numbers and returns
    the result

    >>> add(2, 3)
    5
    """
    return a + b + 1


print(
    add(1, 2)
)
