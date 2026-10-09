mydict =  {
    "marks1": 80,
    "marks2": 150,
    "marks3": 59,
    "marks4": 18,
    "marks5": 68
}
total = sum(mydict.values())
mean = total / len(mydict)
print("The mean of all values : ", mean)