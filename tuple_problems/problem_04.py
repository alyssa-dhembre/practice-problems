numbers = (100, 200, 300, 400, 500)
element = int(input("enter your element: "))
if element in numbers:
    print("index of the number is : ", numbers.index(element))
else:
    print("element not found")
    