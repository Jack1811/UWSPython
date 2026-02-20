# Session 2: Introduction to Python II
## Section 1: Comparisons and Conditionals

### Exercise 1: Comparison Operators

Began learning about and using comparison operators using W3Schools.

### Exercise 2: Logical Operators

Began learning about and using logical operators using W3Schools.

### Exercise 3: if

Started new file "lab_week_2.py" and copied code into file, changed variable value.

Following code uses age variable to print different output depending on what the variable is set to (If the number is under 18, output is child. If the number is over 18, output is adult)

```python

age = 15
age_group = "child"

if age > 18:
        age_group = "adult"

print(f"The age group is {age_group}")

```

Output

```console
The age group is child
```

### Exercise 4: if-else

Copied code into python file and changed variable.

Following code uses wind speed variable and outputs differently dependent upon what number is defined. (If wind speed is less than 10, output "calm day," otherwise print "windy day")

```python
wind_speed = 5

if wind_speed < 10:
    print("It is a calm day")
else:
    print("It is a windy day")
```

Output

```console
It is a calm day
```

### Exercise 5: if-elif-else

Copied code into python file and changed variable value.

Following code uses grade variable to output different output dependent upon the score relative to the comparison operators. Each statement has a different output.

```python
grade = 5

if grade < 50:
     print("You failed")
elif grade < 60: 
     print("You passed")
elif grade < 70:
     print("You got a good pass")
else:
     print("You got an excellent pass")
```

Output

```console
You failed
```

### Exercise 6: Summary

Created 2 variables (Temp1, Temp2) and assigned different values.

Used an if else statement to compare the two numbers and output a statement dependent upon whether they were equal or not.

```python
Temp1 = 20
Temp2 = 30

if Temp1 == Temp2:
     print("The temperatures are equal")
else:
     print("The temperatures are not equal")
```

Output

```console
The temperatures are not equal
```

## Section 2: Python Lists

### Exercise 1: Creating a list

Created a list of cities containing "Glasgow", "London", and "Edinburgh."

```python
city_list = ["Glasgow", "London", "Edinburgh"]
```

### Exercise 2: Accessing a list

Code prints the third item within the list then uses slicing to print the first two seperately

```python
capital = city_list[2]
others = city_list[0:2]

print(capital)
print(others)
```

Output

```console
Edinburgh
['Glasgow', 'London']
```

### Exercise 3: Modifying a list

Added "Manchester" to the list and replaced "London" with Birmingham

```python
city_list.append("Manchester")
city_list[1] = "Birmingham"

print(city_list)
```

Output

```console
['Glasgow', 'Birmingham', 'Edinburgh', 'Manchester']
```

### Exercise 4: Summary

Created list "colours" containing 3 colours as strings.

List is printed, then second colour is printed using seperate variable "red_colour"

First colour ("blue") is changed to "orange."

Length of list is printed.

Conditional if statement used to check whether "red" is in the list" and outputs accordingly.

Used slicing to create a new list called "selected_colours" containing only the second and third colours, then printed it.

```python
colour_list = ["blue", "red", "white"]
print(colour_list)

red_colour = colour_list[1]
print(red_colour)

colour_list[0] = "orange"
print(colour_list)

colour_list_length = len(colour_list)
print(colour_list_length)

if "red" in colour_list :
     print("Red is in the list")
else:
     print("Not in the list")

selected_colours = colour_list[1:3]
print(selected_colours)
```

Output

```console
['blue', 'red', 'white']
red
['orange', 'red', 'white']
3
Red is in the list
['red', 'white']
```

## Section 3: Python Loops

### Exercise 1: While Loops

Used W3Schools to learn about and start using while loops.

### Exercise 2: For Loops

Used city_list from earlier and printed each city using a for loop

```python
for city in city_list:
     print(city)
```

Output

```console
Glasgow
Birmingham
Edinburgh
Manchester
```

### Exercise 3: Loop Keywords: Range, break and continue.

Used for loop to print numbers 0 through 4, but stops when the loop reaches 3.

```python
for i in range(5): 
     print(i) 
     if i == 3: 
          break
```

Output

```console
0
1
2
3
```

### Exercise 4: Summary Tasks

#### Task 1: Even Numbers

Created a list "numbers" which contains numbers 1-10.
Used a for loop to only print even numbers

```python
numbers = list(range(1, 11))

for num in numbers:
     if num % 2 == 0:
          print(num)
```

Output

```console
2
4
6
8
10
```

#### Task 2: Sum of Squares

Created variable "sum_of_squares" and set it to 0.

Used a for loop to iterate through numbers 1-5.

Added the square of each number.

Printed the final value of "sum_of_squares."

```python
sum_of_squares = 0

for num in range(1, 6):
     sum_of_squares += num ** 2 
print(sum_of_squares)
```

Output

```console
55
```

#### Task 3: Countdown

Created variable "countdown" and set it to 10.

Used a while loop to iterate and print a countdown to the number 1.

Once the countdown = 0, prints "Liftoff!"

```python
countdown = 10

while countdown > 0:
     print(countdown)
     countdown -= 1
     
print("Liftoff!")
```

Output

```console
10
9
8
7
6
5
4
3
2
1
Liftoff!
```

## Section 4: Obtaining User Input

### Exercise 1: User Input

#### Task 1: User Input and Conditional Statements

Used input to create value "age" and made it an integer.

Used if and elif statements to output a different statement dependent upon the age input

```python
age = input("How old are you? ")

age = int(age)

if age < 18:
     print("You are a minor")
elif age > 18:
     print("You are an adult")
elif age > 65:
     ("You are a senior citizen")
```

Output

```console
How old are you? 15
You are a minor
```

#### Task 2: Temperature Convertor

Used previously created temperature convertor and modified it to take user input. 

User inputs a temperature in celsius and allows them to chose which temperature to convert to (Fahrenheit or Kelvin.)

```python
celsius_input = input("Enter a Temperature in Celsius: ")
celsius_float = float(celsius_input)

temp_convertor = input("What would you like to convert to? Please enter F or K: ")

print("Welcome to the Temperature Converter")
print("The temperature you have entered is ", celsius_input, " degree Celsius.")
print("Converted Temperatures")

if temp_convertor == "F":
    degree_f = celsius_float * 9/5 + 32
    degree_f_decimal = "{:.2f}".format(degree_f)
    print("You have chosen Farenheit.")
    print(celsius_input, "degree Celsius is equal to ", degree_f_decimal, " Fahrenheit.")    

if temp_convertor == "K":
    degree_k = celsius_float + 273.15
    print("You have chosen Kelvin.")
    print(celsius_input, "degree Celsius is equal to ", degree_k, "Kelvin.")


print("Thank you for using the Temperature Converter!")
```

Output

```console
Enter a Temperature in Celsius: 15
What would you like to convert to? Please enter F or K: F
Welcome to the Temperature Converter
The temperature you have entered is  15  degree Celsius.
Converted Temperatures
You have chosen Farenheit.
15 degree Celsius is equal to  59.00  Fahrenheit.
Thank you for using the Temperature Converter!
```