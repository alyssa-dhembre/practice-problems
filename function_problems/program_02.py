
def Add(x, y):
    return x + y

def Subtract(x, y):
    return x - y

def Multiply(x, y):
    return x * y

def Divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    print("Result:", Add(x, y))
elif choice == 2:
    print("Result:", Subtract(x, y))
elif choice == 3:
    print("Result:", Multiply(x, y))
elif choice == 4:
    print("Result:", Divide(x, y))
else:
    print("Invalid choice")
