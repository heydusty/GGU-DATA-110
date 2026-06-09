# Code 11: Nested If Statements
# An if/elif/else inside another if block.
# Inner else must match the inner if, not the outer block.

num = int(input("Enter your number: "))

if num > 0:
    print("The number is positive")
    if num % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")
elif num < 0:
    print("The number is negative")
else:
    print("The number is Zero")
