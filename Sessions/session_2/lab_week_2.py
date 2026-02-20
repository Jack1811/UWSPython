#Session 2 Section 1

#%%
# Exercise 3
# age = 19
age = 15
age_group = "child"

if age > 18:
        age_group = "adult"

print(f"The age group is {age_group}")

#%%
#Exercise 4
# wind_speed = 30
wind_speed = 5

if wind_speed < 10:
    print("It is a calm day")
else:
    print("It is a windy day")

#%%
#Exercise 5

# grade = 55
# grade = 65
# grade = 75
grade = 5

if grade < 50:
     print("You failed")
elif grade < 60: 
     print("You passed")
elif grade < 70:
     print("You got a good pass")
else:
     print("You got an excellent pass")

#%%
#Exercise 6
Temp1 = 20
Temp2 = 30

if Temp1 == Temp2:
     print("The temperatures are equal")
else:
     print("The temperatures are not equal")

#%%
#Session 2 Section 2
#Exercise 1

city_list = ["Glasgow", "London", "Edinburgh"]

#%%
#Exercise 2
capital = city_list[2]
others = city_list[0:2]

print(capital)
print(others)

#%%
#Exercise 3
city_list.append("Manchester")
city_list[1] = "Birmingham"

print(city_list)

#%%
#Exercise 4
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

#%%
#Section 3
#Exercise 2
city_list = ["Glasgow", "London", "Edinburgh"]

for city in city_list:
     print(city)

#%%
#Exercise 3
for i in range(5): 
     print(i) 
     if i == 3: 
          break


#%%
#Exercise 4
#Task 1
numbers = list(range(1, 11))

for num in numbers:
     if num % 2 == 0:
          print(num)

#%%
#Task 2
sum_of_squares = 0

for num in range(1, 6):
     sum_of_squares += num ** 2 
print(sum_of_squares)


#%%
#Task 3
countdown = 10

while countdown > 0:
     print(countdown)
     countdown -= 1
     
print("Liftoff!")

#%%
#Section 4
age = input("How old are you? ")

age = int(age)

if age < 18:
     print("You are a minor")
elif age > 18:
     print("You are an adult")
elif age > 65:
     ("You are a senior citizen")
