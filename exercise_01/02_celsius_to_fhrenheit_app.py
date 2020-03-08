# 2. Celsius to Fahrenheit (°C to °F) App
# Write a console programme that
# (1) Allows users to enter a number as temperature in Celsius
# (2) Makes sure what users entered is valid
# (3) Prints the temperature in Fahrenheit

from helper.numeric_helper import NumericChecker

numeric_checker = NumericChecker()
print("Exercise 01_02: Celsius to Fahrenheit (°C to °F) App")
celsius = "a"

while not(numeric_checker.isfloat(celsius)):
  celsius = input("Enter temperature in celsius: ")

celsius = float(celsius)

fahrenheit = (celsius * 9/5) + 32

print("{} Celsius is: {} Fahrenheit".format(celsius, fahrenheit))
