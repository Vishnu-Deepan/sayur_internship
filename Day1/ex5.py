# problem #5
# In your college Python is taught in 3 different departments by the same professor. 
# For each dept, get the no of students stutying Python and their marks in the final exam 
# Get the input as comma seperated string

# Find the top 3 marks in each class
# Find the top 3 marks if all classes are combined.
# Find the avg mark of students with passing mark in each class and the classes combined.
# Find which class has the best average mark and least number of failed students.


# Problem #5
pass_mark = 50  
dept_data = []

for _ in range(3):  
    dept_name = input("Enter the department name: ")
    input_str = input(f"Enter marks(comma-separated): ")
    marks = list(map(int, input_str.split(',')))

    top_3 = sorted(marks, reverse=True)[:3]
    avg_passing = sum(mark for mark in marks if mark >= pass_mark) / len(marks)
    failed_students_count = len([mark for mark in marks if mark < pass_mark])

    dept_data.append((dept_name, top_3, avg_passing, failed_students_count))

all_marks_combined = [mark for _, marks, _, _ in dept_data for mark in marks]
top_3_combined = sorted(all_marks_combined, reverse=True)[:3]

best_avg_dept = min(dept_data, key=lambda x: x[2])
least_failed_dept = min(dept_data, key=lambda x: x[3])

for dept_name, top_3, avg_passing, failed_students_count in dept_data:
    print(f"\nDepartment {dept_name}:")
    print(f"Top 3 marks: {top_3}")
    print(f"Avg mark of students with passing mark: {avg_passing}")
    print(f"Number of failed students: {failed_students_count}")

print("\nCombined Classes:")
print(f"Top 3 marks: {top_3_combined}")
print(f"Avg mark of students with passing mark: {sum(all_marks_combined) / len(all_marks_combined)}")

print("\nDepartment with the best average mark:")
print(f"Top 3 marks: {best_avg_dept[1]}")
print(f"Avg mark of students with passing mark: {best_avg_dept[2]}")

print("\nDepartment with the least number of failed students:")
print(f"Top 3 marks: {least_failed_dept[1]}")
print(f"Avg mark of students with passing mark: {least_failed_dept[2]}")
