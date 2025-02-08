"""create a NumPy array of shape (4, 4) containing numbers from 1 to 16. Use slicing to extract for
the given conditions"""
import numpy as np
array = np.arange(1, 17).reshape(4, 4)
print("Original 4x4 Array:")
print(array)
subarray_1 = array[:2, :2]
print("\nFirst two rows and first two columns:")
print(subarray_1)
subarray_2 = array[2:, 2:]
print("\nLast two rows and last two columns:")
print(subarray_2)
subarray_3 = array[1:3, 1:3]
print("\nMiddle 2x2 subarray:")
print(subarray_3)