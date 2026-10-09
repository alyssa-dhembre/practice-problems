name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

maths = float(input("Enter Maths Marks: "))
physics = float(input("Enter Physics Marks: "))
chemistry = float(input("Enter Chemistry Marks: "))

# Find highest marks
highest = max(maths, physics, chemistry)

print("\nSubject(s) with Highest Marks:")

if maths == highest:
    print("Maths")
if physics == highest:
    print("Physics")
if chemistry == highest:
    print("Chemistry")

# Find lowest marks
lowest = min(maths, physics, chemistry)

print("\nSubject(s) with Lowest Marks:")

if maths == lowest:
    print("Maths")
if physics == lowest:
    print("Physics")
if chemistry == lowest:
    print("Chemistry")