number = 1
if number > 5:
    raise Exception(f"The number should not exceed 5. ({number=})")
print(number)


# Here’s another example where you open a file and use a built-in exception:
try:
    with open("file.log") as file:
        read_data = file.read()
except:
    print("Couldn't open file.log")


try:
    with open("file.log") as file:
        read_data = file.read()
except FileNotFoundError as fnf_error:
    print(fnf_error)


def func(a):
    if a < 4:
        b = a/(a-3)
    print("Value of b = ", b)

try:
    func(6)
    func(3)
except ZeroDivisionError:
    print("ZeroDivisionError Occurred and Handled")
except NameError:
    print("NameError Occurred and Handled")


try:
    even_numbers = [2,4,6,8]
    print(even_numbers[2])
except ZeroDivisionError:
    print("Denominator cannot be 0.")
except IndexError:
    print("Index Out of Bound.")
