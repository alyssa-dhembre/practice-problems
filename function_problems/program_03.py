def largest_of_three(x, y, z):
    list = [x, y, z]
    list.sort()
    print(list[2])

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

print("largest : ", end="")
largest_of_three(x, y, z)
