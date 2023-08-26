# Create a dictionary mapping students' names to their respective marks
student_marks = {
    "Asish": 85,
    "LN": 92,
    "Ankit": 78,
    "Rajat": 88,
    "Soujanya": 80
}

# A. Add a new student and their marks to the dictionary
new_student_name = "Sumit"
new_student_marks = 80
student_marks[new_student_name] = new_student_marks

# B. Calculate the average marks of all students
total_marks = sum(student_marks.values())
num_students = len(student_marks)
average_marks = total_marks / num_students

# C. Find the students with the highest marks
highest_marks = max(student_marks.values())
students_with_highest_marks = [name for name, marks in student_marks.items() if marks == highest_marks]

# D. Sort the dictionary by students' names in alphabetical order
sorted_student_marks = {name: marks for name, marks in sorted(student_marks.items())}

# Print the updated dictionary, average marks, and students with the highest marks
print("Updated student marks dictionary:", student_marks)
print("Average marks of all students:", average_marks)
print("Students with the highest marks:", students_with_highest_marks)
print("Sorted student marks dictionary by names:", sorted_student_marks)
