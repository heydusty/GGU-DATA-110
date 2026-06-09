# Code 3: Basic Data Types and Type Conversion

# int, float, str
a = 23
b = 23.5
c = "23.5"

print(type(a))   # <class 'int'>
print(type(b))   # <class 'float'>
print(type(c))   # <class 'str'>

# bool
t = True
f = False
print(type(t))   # <class 'bool'>

print(t or f)    # True
print(t and f)   # False

# int + float = float (implicit type conversion)
a = 20
b = 20.5
c = a + b
print(type(c))   # <class 'float'>
print(c)         # 40.5

# Explicit type conversion
p = "10"
q = 5

# Cannot add str and int directly:
# r = p + q  ->  TypeError: can only concatenate str (not "int") to str

r = int(p) + q   # Convert string to int first
print(r)         # 15

s = p + str(q)   # Concatenate as strings
print(s)         # 105
