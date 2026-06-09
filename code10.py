# Code 10: If-Elif-Else (Grade Calculator)
# elif and else must be at the SAME indentation level as if

marks = int(input("Enter your marks: "))

if marks < 60:
    print("Your grade is F")
elif marks < 70:
    print("Your grade is D")
elif marks < 80:
    print("Your grade is C")
elif marks < 90:
    print("Your grade is B")
else:
    print("Your grade is A")
