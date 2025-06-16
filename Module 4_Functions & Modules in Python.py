def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers."
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Take input from user
number = int(input("enter a number = "))
fact = factorial(number)
print(f"factorial of {number} is {fact}")
