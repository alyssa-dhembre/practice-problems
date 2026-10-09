students = {
    "Mona": 89,
    "kriyan": 100,
    "taksh": 99,
    "Mrudula": 99,
    "alyssa": 99
}
highest_student = max(students, key=students.get)
print("Student with highest marks = ", highest_student)
print("Highest marks = ", students[highest_student])