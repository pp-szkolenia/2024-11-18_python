def divide(a: float, b: float):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return None


print(divide(2, 0))

# ---


y = 1

try:
    x = 1
    z = y + "."
except (NameError, TypeError) as e:
    print("Wystąpił błąd: ", type(e), " | ", e)


try:
    x = 1
    z = y + "."
except NameError:
    print("Wystąpił NameError")
except TypeError:
    print("WYstąpił TypeError")

try:
    x = 1
    z = y + "."
except (NameError, TypeError) as e:
    print("Wystąpił błąd: ", type(e), " | ", e)
else:
    print("Nie było błędu")

connection = open_db_connection()

try:
    connection.save_to_database(data)
except Exception as e:
    connection.rollback()
finally:
    connection.close()
