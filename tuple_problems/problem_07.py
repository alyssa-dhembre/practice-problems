numbers = (100,200,300,400,500)
tuple = (numbers[-1],) + numbers[1:-1] + (numbers[0],)
print("Original tuple : ", numbers)
print("Modified tuple : ", tuple)
