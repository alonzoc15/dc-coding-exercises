temp_celsius = float(input('Temperature in Celsius to convert to Fahrenheit? '))
temp_fahrenheit = temp_celsius * 1.8 + 32

# Use string interpolation to print off custom message to user

print('%.2f degrees Celsius is equivalent to %.2f degrees Fahrenheit' % (temp_celsius, temp_fahrenheit))