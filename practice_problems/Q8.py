a = int(input("Enter your number : "))
fact =1
i= 1
while(i<=a):
    fact = fact * i
    i+=1
print(fact)

# OR

a = int(input("Enter your number : "))

fact = 1
for i in range(1, a+1):
    fact = fact *i
print(fact)