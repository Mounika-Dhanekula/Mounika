"""Create two NumPy arrays of the same shape, A and B. Perform the following arithmetic operations:
Element-wise addition.
Element-wise subtraction.
Element-wise multiplication.
Element-wise division."""
import numpy as np

# Create two NumPy arrays A and B of shape (3, 3)
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

B = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])
addition_result = A + B
subtraction_result = A - B
multiplication_result = A * B
division_result = A / B
print("Array A:")
print(A)
