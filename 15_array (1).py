"""Write a Python program to create a 5x5 NumPy array of random integers and Perform array
indexing as given"""
import numpy as np
random_array = np.random.randint(1, 101, size=(5, 5))

print("Original 5x5 Array of Random Integers:")
print(random_array)
first_element = random_array[0, 0]
print("\nElement at first row, first column:", first_element)
second_row = random_array[1, :]
print("\nSecond row:", second_row)
third_column = random_array[:, 2]
print("\nThird column:", third_column)
subarray = random_array[1:3, 2:4]
print("\nSubarray from rows 1 to 2 and columns 3 to 4:")
print(subarray)