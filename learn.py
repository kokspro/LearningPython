# print("Hello World!\n" * 3)

# first = "Will"
# last = "Koks"
# full = f"{first} {last}"
# print(full)

# LOOPS
# for number in range(3):
#     print(f"{number} {full}")
#     print("Testing", (number + 1) * "." )

# success = False
# for number in range(3):
#     print("Attempting...")
#     if success:
#         print("Success!")
#         break
# else:
#     print("Attempted 3 times but failed")

# for x in "Oh wow, this is cool":
#     print(x)

# exercise
# counter = 0
# for x in range(1, 10):
#     if x % 2 == 0:
#         print(x)
#         counter += 1

# print(f"We have {counter} even numbers")

# FUNCTIONS
# def greet():
#     name = input("What is your name?: ")
#     print(f"Hello, {name}.")
#     print("Welcome to Python!")

# greet()

# parameter = something, something will be the default
# def increment(number, by = 1):
#     return number + by

# print(increment(2))

#unknown number of arguments
# def multiply_lists(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total

# print(multiply_lists(1, 2, 3, 4))

# **numbers would make it a dictionary
# dictionaries save key value pairs

# def save_user(**user):
#     print(user["name"])
#     print(user["id"])
#     print(user["age"])

# save_user(id = 1, name = "William", age = 39)

# Exercise
def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input

print(fizz_buzz(9))
print(fizz_buzz(10))
print(fizz_buzz(15))
print(fizz_buzz(19))
