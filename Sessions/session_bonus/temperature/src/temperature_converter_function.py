# Temperature Converter
# This program converts temperature from Celsius to Fahrenheit and Kelvin.
scales = ["C", "F", "K"]

MIN_VALUES = {
    "C": -273.15,
    "F": -459.67,
    "K": 0.0
}

def convert(temperature_scale: str = "C", temperature_input: str = "0"):
    temperature_scale = temperature_scale.upper()

    if temperature_scale not in scales:
        temperature_scale = "C"
        temperature_input = "0"

    try:
        value = float(temperature_input)
    except ValueError:
        value = 0.0

    if value < MIN_VALUES[temperature_scale]:
        value = MIN_VALUES[temperature_scale]

    if temperature_scale == "C":
        degree_celsius = value
        degree_fahrenheit = (value * 9/5) + 32
        degree_kelvin = value + 273.15

    elif temperature_scale == "F":
        degree_fahrenheit = value
        degree_celsius = (value - 32) * 5/9
        degree_kelvin = (value + 459.67) * 5/9

    elif temperature_scale == "K":
        degree_kelvin = value
        degree_celsius = value - 273.15
        degree_fahrenheit = (value - 273.15) * 9/5 + 32

    return degree_celsius, degree_fahrenheit, degree_kelvin


# The next line prevents the code from being run if called ba a test
if __name__ == "__main__":
    temperature_scale = ("Enter the temperature scale you want to convert from: \n 'C' Celcius \n 'F' Fahrenheit \n 'K'. Kelvin \n")
    temperature_scale = input(temperature_scale).strip().upper()
    if temperature_scale not in scales:
        print("Invalid scale. Please enter 'C', 'F', or 'K'.")
        exit()

    temperature_input = input(f"Enter the temperature in {temperature_scale}: ")
    degree_celcius, degree_fahrenheit, degree_kelvin = convert (temperature_scale, temperature_input)
    print("Temperature Conversion Results:")
    print(f"{degree_celcius} degree Celsius")
    print(f"{degree_fahrenheit} degree Farenheit")
    print(f"{degree_kelvin} degree Kelvin")
    print("Thank you for using the Temperature Converter!")