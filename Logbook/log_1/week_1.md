# Session 1: Introduction to Python I

## Section 1: Setting up a Code Editor and Running Python Scripts

Set up VSCode and installed Python and relevant Python plugins to VSCode. Established folder structure.

## Section 2: Python Syntax Introduction

### Exercise 1: Task 1: Variables and Types

Started new file "lab_week1_part2.py" and copied code into file.

Code defines variable types and prints their type.

```python

var_1 = True #Type = Boolean
var_2 = 1 #Type= Int
var_3 = 3.14159 #Type = Float
var_4 = "Hello World" #Type = String

print(type(var_1))
print(type(var_2))
print(type(var_3))
print(type(var_4))

```

Output

```console
<class 'bool'>
<class 'int'>
<class 'float'>
<class 'str'>
```

### Exercise 1: Task 2: Casting Variables

Created variables and assigned them values and printed those variables.

Then casted those variables to new variable types and printed the new values.

```python
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
```

Output

```console
5
5.5
True
```

### Exercise 2: Task 1: Arithmetic Operators

Started using Python arithmetic operators

Copied code that calculates multiple sums using different operators and prints the results.

```python
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
```

Output

```console
Addition: 15
Subtraction: 12
Multiplication: 24
Division: 5.0
Floor Division: 4
Modulus: 1
Exponentation: 8
```

### Exericse 2: Task 2: Calculating the Average

Created 3 values with numeric values and calculated their average using arithmetic operators and output the result.

```Python
num1 = 11
num2 = 18
num3 = 22

average = (num1 + num2 + num3) / 3

print("Number 1:", num1)
print("Number 2:", num2)
print("Number 3: ", num3)
print("Average:", average)
```

Output

```Console
Number 1: 11
Number 2: 18
Number 3:  22
Average: 17.0
```

### Exercise 2: Task 3: Area of a Rectangle

Created 2 numeric variables called 'length' and 'width' and multiplied them to calculate the area of a rectangle.

```Python
length = 19
width = 25

area = length * width

print("length: ", length)
print("Width: ", width)
print("Area: ", area)
```

Output

```
length:  19
Width:  25
Area:  475
```

### Exericse 3: Task 1: Modify Strings

Created a new string variable and printed it. Then applied multiple modifications to the string and output the modified versions. Also output the length of the string.

```python
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
```

Output 

```
This class covers ISD.
THIS CLASS COVERS ISD.
this class covers isd.
This class covers Interactive Software Design.
22
```

### Exercise 3: Task 2: f-Strings

Created string variables to store, name, number of courses and campus. Then created an f-string to output the text.

```python
my_name = "Jack"
number_of_classes = 3
campus = "Paisley"

my_test = f"My name is {my_name} and I am studying {number_of_classes} classes in {campus}"

print(my_test)
```

Output

```console
My name is Jack and I am studying 3 classes in Paisley
```

## Section 2: First Program in Python

Created a python program that allows a user to convert celsius to fahrenheit and kelvin, then outputs the result.

```python
celsius_input = 30
celsius_float = float(celsius_input)
degree_f = celsius_float * 9/5 + 32
degree_k = celsius_float + 273.15

degree_f_decimal = "{:.2f}".format(degree_f)

print("Welcome to the Temperature Converter")

print("The temperature you have entered is ", celsius_input, " degree Celsius.")

print("Converted Temperatures")
print(celsius_input, "degree Celsius is equal to ", degree_f_decimal, " Fahrenheit.")
print(celsius_input, "degree Celsius is equal to ", degree_k, "Kelvin.")

print("Thank you for using the Temperature Converter!")

```

Output

```console
Welcome to the Temperature Converter
The temperature you have entered is  30  degree Celsius.
Converted Temperatures
30 degree Celsius is equal to  86.00  Fahrenheit.
30 degree Celsius is equal to  303.15 Kelvin.
Thank you for using the Temperature Converter!
```
