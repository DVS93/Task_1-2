import math

# Ask the user for input
number = float(input("Enter a number = "))

# Perform calculations using the math module
sqrt_result = math.sqrt(number)
log_result = math.log(number)   # natural logarithm (base e)
sine_result = math.sin(number) # sine expects radians

# Display the results
print(f"Square root : {sqrt_result}")
print(f"Logarithm : {log_result}")
print(f"Sine : {sine_result}")
