# Session 1 Section 2 Python Intro

#%%
# Exercise 1 task: Variables and Types

var_1 = True #Type = Boolean
var_2 = 1 #Type= Int
var_3 = 3.14159 #Type = Float
var_4 = "Hello World" #Type = String

print(type(var_1))
print(type(var_2))
print(type(var_3))
print(type(var_4))

#%%
# Exercise 2 task 2: Casting Variables

my_int = 5
my_float = 5.5
my_bool = True

print(my_int)
print(my_float)
print(my_bool)

my_int_float = float(5)
my_float_int = int(5.5)
my_bool_int = int(True)

print(my_int_float)
print(my_float_int)
print(my_bool_int)

#%%
#Exercise 2 Arithmetic Operators
#Addition
result_addition = 10 + 5
print("Addition:", result_addition)

#Subtraction
result_subtraction = 20 - 8
print("Subtraction:", result_subtraction)

#Multiplication
result_multiplication = 6 * 4
print("Multiplication:", result_multiplication)

#Division
result_division = 15 / 3
print("Division:", result_division)

#Floor Division
result_floor_division = 17 // 4
print("Floor Division:", result_floor_division)

#Modulus
result_modulus = 17 % 4
print("Modulus:", result_modulus)

#Exponentiation
result_exponentation = 2 ** 3
print("Exponentation:", result_exponentation)

#%%
#Exercise 2 Task 2

num1 = 11
num2 = 18
num3 = 22

average = (num1 + num2 + num3) / 3

print("Number 1:", num1)
print("Number 2:", num2)
print("Number 3: ", num3)
print("Average:", average)

#%%
#Exercise 2 Task 3

length = 19
width = 25

area = length * width

print("length: ", length)
print("Width: ", width)
print("Area: ", area)

#%%
#Exercise 3 Task 1

my_string = "This class covers ISD."

print(my_string)

my_uppercase_string = my_string.upper()
my_lowercase_string = my_string.lower()
my_new_string = my_string.replace("ISD", "Interactive Software Design")
my_string_length = len(my_string)

print(my_uppercase_string)
print(my_lowercase_string)
print(my_new_string)
print(my_string_length)

#%%
#Exercise 3 Task 2

my_name = "Jack"
number_of_classes = 3
campus = "Paisley"

my_test = f"My name is {my_name} and I am studying {number_of_classes} classes in {campus}"

print(my_test)
