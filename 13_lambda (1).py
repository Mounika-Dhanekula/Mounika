"""Write a Python script that uses a lambda function to calculate the product of two numbers provided
by the use"""
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
product = lambda x, y: x * y
result = product(num1, num2)
print(f"The product of {num1} and {num2} is: {result}")
