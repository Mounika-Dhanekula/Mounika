"""Create a dictionary that stores the names of 3 students as keys and their marks in mathematics as
values. Perform the given operations"""
students_marks = {"Alice": 85, "Bob": 78, "Charlie": 92}
print("Students and their marks:", students_marks)
print("Marks of Alice:", students_marks["Alice"]) 
students_marks["David"] = 88  
print("After adding David:", students_marks)
del students_marks["Bob"]  
print("After removing Bob:", students_marks)