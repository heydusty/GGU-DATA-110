# Code 5: Tuples
# Tuples are immutable and ordered. Once created, elements cannot be changed.

mylist = ("Daawer", "Wasiulla", "Raj", "Ritesh")
print(type(mylist))   # <class 'tuple'>

# Accessing elements by index
print(mylist[0])      # Daawer
print(mylist[1:3])    # ('Wasiulla', 'Raj')

# Tuples are immutable - you cannot reassign elements:
# mylist[0] = "Umar"  ->  TypeError: 'tuple' object does not support item assignment

# Tuples cannot use list methods like .append():
# mylist.append("Riya")  ->  AttributeError: 'tuple' object has no attribute 'append'

# A tuple CAN contain a mutable list inside it
Var3 = ("Ram", "Shyam", [1, 2, 3, 4, 5], 25, 25.5)
print(len(Var3))    # 5
print(Var3[0])      # Ram
print(Var3[2])      # [1, 2, 3, 4, 5]

# The inner list IS mutable even inside a tuple
Var3[2][1] = 20
print(Var3)         # ('Ram', 'Shyam', [1, 20, 3, 4, 5], 25, 25.5)
