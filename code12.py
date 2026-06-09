# Code 12: For Loops

# Basic for loop over a list
mymarks = [86, 89, 77, 78, 76]
for mark in mymarks:
    print(mark)

# Operation inside the loop
for mark in mymarks:
    print(mark * 5)

# Running total (use a different name to avoid shadowing built-in sum())
total = 0
for mark in mymarks:
    total = total + mark
    print(total)

# enumerate - get both index and value
students = ["Afifa", "Saaketh", "Karanveer", "Asmit", "Yuvraj", "Vardhan"]
for ind, stu in enumerate(students):
    print(ind, stu)

# Multiplication table using range()
num = int(input("Enter the number: "))
for i in range(1, 11):
    result = num * i
    print(f"{num} X {i} = {result}")
