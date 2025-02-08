"""Write a Python function called find_largest() that takes a list of numbers as input and returns the
largest number from the list. Test the function with a sample list"""
def find_largest(numbers_list):
    return max(numbers_list)
sample_list = [12, 45, 78, 23, 56]
largest_number = find_largest(sample_list)
print("The largest number in the list is:", largest_number)
