# Code 14: Break, Continue, and Pass Statements

# break - exits the loop immediately when condition is met
print("--- break ---")
for letters in "MachineLearning":
    print(letters)
    if letters == "L":
        break
print("This is the break statement - loop stopped at L")

print()

# continue - skips the current iteration and moves to the next
print("--- continue ---")
for letters in "MachineLearning":
    if letters == "L":
        continue    # Skip printing "L"
    print(letters)

print()

# pass - does nothing; used as a placeholder when a block is required
print("--- pass ---")
for letters in "MachineLearning":
    if letters == "L":
        pass        # Placeholder - no action taken for "L"
    print(letters)  # Still prints every letter including "L"
