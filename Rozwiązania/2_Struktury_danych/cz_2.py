my_list = [1, 1, 2, 3, 5]
my_tuple = (2, 4, 6)
my_set = {"sin", "cos", "tg", "ctg"}

my_dict = {
    "my_list": my_list,
    "my_tuple": my_tuple,
    "my_set": my_set
}

print(len(my_list))

my_list.append(8)

my_list.sort(reverse=True)

my_list.pop(3)
my_list.pop()

my_list *= 3
print(my_list)

# ---
print(len(my_tuple))
print(my_tuple.index(4))
print(my_tuple.count(5))

# ---

print(len(my_dict))
my_dict['a'] = "string"
my_dict["b"] = 123

print(my_dict.get("my_list"))
print(my_dict.get("my_dict", 0))

new_list = [1, 2, 5, 2.242, 12, -3]
print(min(new_list))
print(max(new_list))
print(sum(new_list))

print(sum(new_list) / len(new_list))
print(any(new_list))
print(all(new_list))
