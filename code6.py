# Code 6: Sets
# Sets are unordered, contain no duplicate values, and are mutable.

mys = {"Mango", "Pineapple", "Watermelon", "Guava", "mango", "Mango"}
print(mys)   # Duplicates removed; "Mango" and "mango" are different (case-sensitive)

Var1 = {"Mango", "Banana", "Pineapple", "Apple", "apple", "Apple", "Mango"}
Var2 = {"Apple", "Banana", "Grapes", "Grapes", "Kiwi", "Kiwi", "Orange"}

# Union - all unique elements from both sets
print(Var1.union(Var2))

# Intersection - elements common to both sets
print(Var1.intersection(Var2))

# Difference - elements in Var1 but NOT in Var2
print(Var1.difference(Var2))

# Difference - elements in Var2 but NOT in Var1
print(Var2.difference(Var1))

# Add an element
Var1.add("Kiwi")
print(Var1)
