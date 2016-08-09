import part1

print('test1')
instruction = part1.interpretInstructions('turn on 489,959 through 759,964')
print('correct lighting instructions: ' + str(instruction[0]== 1))
print('correct starting Coord: ' + str(instruction[1] == 489 and instruction[2] == 959))
print('correct ending Coord: ' + str(instruction[3] == 759 and instruction[4] == 964))

print('\ntest2')
instruction = part1.interpretInstructions('toggle 120,314 through 745,489')
print('correct lighting instructions: ' + str(instruction[0]== -1))
print('correct starting Coord: ' + str(instruction[1] == 120 and instruction[2] == 314))
print('correct ending Coord: ' + str(instruction[3] == 745 and instruction[4] == 489))