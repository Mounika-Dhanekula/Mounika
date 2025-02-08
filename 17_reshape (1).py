"""Write a Python program that creates a 2D array of shape (6, 2) using np.arange() and then reshapes
it into a 3D array of shape (2, 3, 2). Flatten the reshaped array and print the result"""
import numpy as np
array_2d = np.arange(1, 13).reshape(6, 2)
print("Original 2D Array (shape 6, 2):")
print(array_2d)
array_3d = array_2d.reshape(2, 3, 2)
print("\nReshaped 3D Array (shape 2, 3, 2):")
print(array_3d)
flattened_array = array_3d.flatten()
print("\nFlattened Array:")
print(flattened_array)