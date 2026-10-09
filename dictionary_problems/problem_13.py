numbers = [100,200,100,300,200,200,100,400,300]
frequency = {}
for num in numbers:
    if num in frequency:
        frequency[num] = frequency[num] + 1
    else:
        frequency[num] = 1
print("The frequency of elements : ", frequency)