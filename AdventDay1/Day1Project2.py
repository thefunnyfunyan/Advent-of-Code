__author__ = 'brandon.runyan'

terribleInstructions = open('terribleInstructions').read()
floor = 0
index = 1
for i in terribleInstructions:
    floor += (1 if i == "(" else -1)
    if floor < 0:
        break
    index += 1
print(index)