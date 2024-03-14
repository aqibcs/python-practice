# Example 1: Add and Remove items from a list in Python
my_list = [0, 1, 2, 3]
my_list.append(4)
print("List: ", my_list)

my_list.insert(5, 5)
print(my_list)

my_list.remove(2)
print(my_list)

popped_element = my_list.pop(0)
print(my_list)
print(popped_element)

# Example 2: Modify item from a dictionary in Python
my_dict = {"name": "Ali", "age": 20}
print("Dictionary: ", my_dict)

new_dict = my_dict
new_dict["age"] = 25

print(new_dict)

# Example 3: Modify item from a Set in Python
my_set = {1, 2, 3}
print("Set: ", my_set)

new_set = my_set
new_set.add(4)

print(new_set)
