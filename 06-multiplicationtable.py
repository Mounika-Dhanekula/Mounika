"""Write a Python program that takes a number as input and prints the multiplication table
for that number (from 1 to 10)"""
number = int(input("Enter an integer: "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
