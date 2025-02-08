"""Create a Pandas DataFrame with the given Name and marks of 3 courses:
Add a new column named 'Total' that represents the sum of all the courses. Add 'Grade' based
on the values of the 'Total'. Print the updated DataFrame with the new 'Total' and 'Grade'
column."""
import pandas as pd

# Create a dictionary with names and marks of three courses
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Course1': [85, 78, 92],
    'Course2': [88, 76, 89],
    'Course3': [90, 80, 85]
}
df = pd.DataFrame(data)
df['Total'] = df['Course1'] + df['Course2'] + df['Course3']
def assign_grade(total):
    if total >= 270:
        return 'A'
    elif total >= 240:
        return 'B'
    elif total >= 210:
        return 'C'
    else:
        return 'D'
df['Grade'] = df['Total'].apply(assign_grade)
print(df)