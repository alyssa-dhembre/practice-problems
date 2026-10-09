#  to make a calculator
a = int(input("enter your first number: "))    
b = int(input("enter your second number: "))    

c = input("choose your operator from +,-,*,/ : ")

if(c=="+"):
    print("sum of the numbers is : ", a+b)
elif(c=="-"):
    print("difference of both the numbers is : ", a-b)
elif(c=="*"):
    print("multiplication of the numbers is : ", a*b)
elif(c=="/"):
    print("division of the numbers is : ", a/b)
else:
    print("enter valid operator!!")