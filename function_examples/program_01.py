
students = []

def add_student():
    name = input("Enter student name: ")
    roll = int(input("Enter roll number: "))
    marks = float(input("Enter marks: "))
    students.append([roll, name, marks])
    print("Student added successfully!")

def display_students():
    if not students:
        print("No students found")
    else:
        for s in students:
            print("Roll:", s[0], "Name:", s[1],
                  "Marks:", s[2])

def search_student():
    roll = int(input("Enter roll number: "))
    for s in students:
        if s[0] == roll:
            print("Student found:", s)
            return
    print("Student not found")

def average_marks():
    if not students:
        print("No students found")
        return

    total = sum(s[2] for s in students)
    avg = total / len(students)
    print("Average marks:", avg)

def find_topper():
    if not students:
        print("No students found")
        return

    topper = max(students, key=lambda s: s[2])
    print("Topper:", topper[1])
    print("Marks:", topper[2])

while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Average Marks")
    print("5. Find Topper")
    print("6. Exit")

    choice = int(input("Enter your choice (1-6): "))

    if choice == 1:
        add_student()
    elif choice == 2:
        display_students()
    elif choice == 3:
        search_student()
    elif choice == 4:
        average_marks()
    elif choice == 5:
        find_topper()
    elif choice == 6:
        print("Exiting...")
        break
    else:
        print("Invalid choice")