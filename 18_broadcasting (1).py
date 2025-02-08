"""Write a Python program to demonstrate broadcasting. Create an array of shape (3, 3) and add a one-
dimensional array of shape (1, 3) to it using broadcasting"""
import numpy as np
array_2d = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])
array_1d = np.array([10, 20, 30])
result = array_2d + array_1d
print("Original 2D Array (shape 3, 3):")
print(array_2d)

print("\n1D Array (shape 1, 3):")
print(array_1d)

print("\nResult after broadcasting and addition:")
print(result)