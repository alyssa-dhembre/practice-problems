numbers = [(1, 2, 4), (4, 5, 6), (7, 8, 9)]
list = []
for tuple in numbers:
    new_tuple = tuple[:-1] + (10,)
    list.append(new_tuple)
print("Original list = ", numbers)
print("New list = ", list)