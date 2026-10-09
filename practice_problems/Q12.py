n = int(input("Enter a number: "))

reverse = 0

while n>0 :
    unit_place = n%10
    reverse = reverse*10 + unit_place
    n=n//10
print("Reverse of the number is : ", reverse)