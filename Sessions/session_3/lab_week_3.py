#Session 3: Section 1


#Exercise 1: Task 1

friend_list = ["John", "Jane", "Jack"]

def greet_friends(friend_list):
    for name in friend_list:
        print(f"Hello {name}!")

greet_friends(friend_list)
# %%

#Exercise 1: Task 2

income = 50000
tax_rate = 0.2

def calculate_tax(income, tax_rate):
    tax_result = income ** tax_rate
    tax_result = round(tax_result, 2)
    print (f"The tax is £{tax_result}")

calculate_tax(income, tax_rate)

# %%

# Exercise 1: Task 3

def compound_interest(principal, duration, interest_rate):
    print(f"Initial investment is: £{principal}")
    if interest_rate < 0 or interest_rate > 1:
        print("Please enter a number between 0 and 1")
        return None

    if duration < 0:
        print("Please enter a positive number of years")
        return None
    
    for year in range(1, duration + 1):
         total_for_the_year = principal * (1 + interest_rate) ** year
         total_for_the_year = round(total_for_the_year, 2)
         print(f"The total for the year {year} is £{total_for_the_year}")

    return int(total_for_the_year)

compound_interest(1000,5,0.03)     
# %%

# Section 2

# Exercise 3: Task 1

assert 1 + 1 == 2

assert 1 + 1 == 3

# %%

#Exercise 4: Task 1

print("Hello World!")

# %%
#Task 2

favorite_color = "Blue"
print("My favorite color is", favorite_color)

# %%
#Task 3

number1 = 5
number2 = 3
result = number1 + number2
print("The sum is:", result)

# %%
#Task 4

fruits = ["apple", "banana", "cherry"]
print(fruits[1])


# %%
#Task 5

time = 11
if time < 12:
    print("Good morning!")  

