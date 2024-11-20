text = "hello world!!!!"

with open("files/text.txt", "w") as f:
    f.write(text)

with open("files/text.txt", "a") as f:
    f.write(text)

with open("files/text.txt", "r") as f:
    text_from_file = f.read()


print(text_from_file)


text_data = [
    "text 1", "text 2", "text 3"
]


with open("files/lista.txt", "w") as f:
    f.writelines([item + "\n" for item in text_data])


with open("files/lista.txt", "r") as f:
    from_file = f.readlines()

print(from_file)


import json
from datetime import date


data = [
    {"a": 1, "b": 2},
    {"a": 10, "b": 3}
]

with open("files/data.json", "w") as f:
    json.dump(data, f, indent=2)


with open("files/data.json", "r") as f:
    from_json = json.load(f)


print(from_json)

data_str = json.dumps(data)
# print(data_str, type(data_str))

from_str = json.loads(data_str)
print(from_str, type(from_str))


import pickle


x = 13131

with open("files/x.pkl", "wb") as f:
    pickle.dump(x, f)

with open("files/x.pkl", "rb") as f:
    y = pickle.load(f)


print(y)
