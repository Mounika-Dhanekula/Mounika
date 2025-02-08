"""Write a Python program to create a one-dimensional, two-dimensional, and three-dimensional
NumPy array. Print the shape and dimensions of each array"""
import numpy as np
one_array = np.array([1, 2, 3, 4, 5])
print("One-dimensional array:")
print(one_array)
print("Shape:", one_array.shape)
print("Dimensions:", one_array.ndim)
two_array = np.array([[1, 2, 3], [4, 5, 6]])
print("\nTwo-dimensional array:")
print(two_array)
print("Shape:", two_array.shape)
print("Dimensions:", two_array.ndim)
three_d_array = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("\nThree-dimensional array:")
print(three_d_array)
print("Shape:", three_d_array.shape)
print("Dimensions:", three_d_array.ndim)
