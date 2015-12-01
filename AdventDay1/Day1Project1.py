__author__ = 'brandon.runyan'

terribleInstructions = open('terribleInstructions').read()

floor = 0
for i in terribleInstructions:
    if i == "(":
        floor += 1
    elif i == ")":
        floor -= 1
print(floor)