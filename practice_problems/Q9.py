a = int(input("Enter your number: "))
count= 0
for i in range(2, a):
    if(a%i==0):
        count=count+1

if(count==0 and a>1):
    print("Prime!!")
else:
    print("Not Prime!!")