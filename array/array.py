# Importing the array module with an alias 'arr'
import array as arr

# Creating an array 'a' of type 'int' with elements from 1 to 9
a = arr.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])

# Printing the newly created array
print("The newly created array is: ", end=" ")
for i in a:
    print(i, end=" ")
print("\n")

# Inserting the value 4 at the second position of the array
a.insert(1, 4)
print("Array after insertion of 4 at index 1: ", end=" ")
for i in a:
    print(i, end=" ")
print("\n")

# Accessing and printing the first and second elements of the array
print("First element: ", a[0])
print("Second element: ", a[1])
print("\n")

# Popping (removing and returning) the element at the second position
popped_element = a.pop(1)
print("Popped element at index 1: ", popped_element)
print("Array after popping: ", end=" ")
for i in a:
    print(i, end=" ")
print("\n")

# Removing the first occurrence of the value 4 from the array
a.remove(4)
print("Array after removing the first occurrence of 4: ", end=" ")
for i in a:
    print(i, end=" ")
print("\n")

# Slicing the array from the 4th to the 8th element (index 3 to 7)
sliced_array = a[3:8]
print("Sliced array (elements in range 3-8): ", end=" ")
for i in sliced_array:
    print(i, end=" ")
print("\n")

# Updating the third element of the array to 6
a[2] = 6
print("Array after updating the third element to 6: ", end=" ")
for i in a:
    print(i, end=" ")
print("\n")
