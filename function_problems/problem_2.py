# calculate sum and product
def sumprod(x,y,z):
    sum = x+y+z
    prod = x*y*z
    return sum, prod
x = int(input("Enter number 1:"))
y = int(input("Enter number 2:"))
z = int(input("Enter number 3:"))

print(sumprod(x,y,z))