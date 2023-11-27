# Problem #2
# you have a list of student names and another list with their marks in CS. 
# hard code the values. no need to get it as input
# Pass mark is 50.
# Print a new list with all the students with pass marks along with their mark in the format name:mark.
# Also print the number of students who failed.

student_names = ["Vishnu", "Sandeep", "Joe", "Tejas"]
marks_cs = [60, 45, 75, 30]

pass_mark = 50
passing_students = [(name, mark) for name, mark in zip(student_names, marks_cs) if mark >= pass_mark]
failed_students_count = len(student_names) - len(passing_students)

print("Passing students:")
for name, mark in passing_students:
    print(name + ":" + str(mark))

print(f"Number of students who failed: {failed_students_count}")
