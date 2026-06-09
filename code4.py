# Code 4: Lists
# Lists are mutable, ordered, and allow duplicate values.

mylist = ["Daawer", "Wasiulla", "Raj", "Ritesh"]
print(type(mylist))   # <class 'list'>

# Append an element
mylist.append("Tessica")
print(mylist)

# Modify element by index
mylist[0] = "Umar"
print(mylist)

# List of favourite cricketers
cricketers = ["Virender Sehwag", "MS Dhoni", "Rohit Sharma"]
print(cricketers)

# Concatenating two lists
Batsman = ["Sachin", "Saurav", "Sehwag", "Virat", "Dhoni"]
Bowlers = ["Bumrah", "Arshdeep", "Shami", "Archer", "Siraj"]

Allplayers = Batsman + Bowlers
print(Allplayers)

# Slicing to remove an element at index 3 ("Virat")
Allplayers = Allplayers[0:3] + Allplayers[4::]
print(Allplayers)

# Remove by value
Allplayers.remove("Shami")
print(Allplayers)

# Slicing from index 3 onwards
print(Allplayers[3::])

# Membership operator
print("Dravid" in Allplayers)   # False
print("Sachin" in Allplayers)   # True

# Append and count
Allplayers.append("Rahul")
print(Allplayers)

print(Allplayers.count("Rahul"))    # 1
print(Allplayers.count("Sachin"))   # 1

# Find index of an element
print(Allplayers.index("Dhoni"))    # 3

# Allplayers.index("Shami") would raise ValueError because Shami was removed
# Use 'in' to check before calling .index()
if "Shami" in Allplayers:
    print(Allplayers.index("Shami"))
else:
    print("Shami is not in the list")

print(len(Allplayers))
