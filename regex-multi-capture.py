import re

target_string = "The price of ice-creams PINEAPPLE 20 MANGO 30 CHOCOLATE 40"

# two groups enclosed in separate ( and ) bracket
# group 1: find all uppercase letter
# group 2: find all numbers
# you can compile a pattern or directly pass to the finditer() method
pattern = re.compile(r"(\b[A-Z]+\b).(\b\d+\b)")

# find all matches to groups
for match in pattern.finditer(target_string):
    # extract words
    print(match.group(1))
    # extract numbers
    print(match.group(2))

for match in pattern.finditer(target_string):