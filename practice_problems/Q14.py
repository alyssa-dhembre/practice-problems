marks = float(input("Enter maths marks: "))
if(marks>100):
    print("enter marks from 0 to 100")
elif(90<=marks<=100):
    print("Grade O")
elif(80<=marks<=89):
    print("Grade A+")
elif(70<=marks<=79):
    print("Grade A")
elif(60<=marks<=69):
    print("Grade B")
elif(50<=marks<=59):
    print("Grade C")
elif(40<=marks<=49):
    print("Grade P")
elif(0<=marks<=39):
    print("Grade F")
else:
    print("enter marks from 0 to 100")
