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

