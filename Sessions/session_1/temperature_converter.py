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

