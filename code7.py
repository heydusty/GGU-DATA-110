# Code 7: Dictionaries
# Dictionaries store key-value pairs. Keys must be unique.

WCwinners = {
    1975: "WestIndies",
    1983: "India",
    1987: "Australia",
    2011: "India"
}

# Access value by key
print(WCwinners[1975])   # WestIndies

# Add a new key-value pair
WCwinners[2023] = "Australia"
print(WCwinners)

# Access all keys and values
print(WCwinners.keys())
print(WCwinners.values())
print(WCwinners.items())
