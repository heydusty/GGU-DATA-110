# Code 15: Nested Loops, Zip, and List Comprehension

# Multiplication tables from 2 to 10 using nested loops
for num in range(2, 11):
    print("Multiplication of", num)
    for i in range(1, 11):
        result = num * i
        print(f"{num} X {i} = {result}")
    print()

# zip() - combine multiple iterables element by element
players = ["Virat", "Aiyer", "Ritesh", "David", "Krunal"]
Runs = [120, 100, 130, 99, 123]
Age = [32, 33, 35, 25, 28]
Todays_Score = [10, 35, 100, 101, 120]

Var_mapped = zip(players, Runs, Age, Todays_Score)
print(list(Var_mapped))

# Unzip using * (splat) operator
players = ["Virat", "Rajat", "Ritesh", "Tim", "Krunal"]
runs = [75, 15, 32, 24, 1]
age = [38, 31, 29, 28, 30]
today_score = [10, 35, 57, 101, 12]

Var_mapped = zip(players, runs, age, today_score)
P, R, A, T = zip(*Var_mapped)

print(P)
print(R)
print(A)
print(T)

# Nested loop - flatten a 2D list into 1D
All_planets = [
    ["Mercury", "Venus", "Earth"],
    ["Mars", "Jupiter", "Saturn"],
    ["Uranus", "Neptune", "Pluto"]
]

single_list = []
for sublist in All_planets:
    for planet in sublist:
        single_list.append(planet)

print(single_list)

# Print all planets using unpacking
print(*All_planets[0], *All_planets[1], *All_planets[2])

# List comprehension - same result in one line
singleList = [planet for sublist in All_planets for planet in sublist]
print(singleList)

# List comprehension with an operation
marks = [23, 24, 25, 26, 27]
print([x + 2 for x in marks])

# Fix: use a separate variable instead of overwriting the list
for mark in marks:
    result = mark + 5
    print(result)
