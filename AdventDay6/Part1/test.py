import part1

def group1():
    print('testing Instruction Interpretation')
    test1()
    test2()

def group2():
    print('\ntesting instruction execution')
    test3()
    print('\n')
    test4()


def test1():
    print('test1')
    instruction = part1.interpretInstructions('turn on 489,959 through 759,964')
    print('correct lighting instructions: ' + str(instruction[0]== 1))
    print('correct starting Coord: ' + str(instruction[1] == 489 and instruction[2] == 959))
    print('correct ending Coord: ' + str(instruction[3] == 759 and instruction[4] == 964))

def test2():
    print('\ntest2')
    instruction = part1.interpretInstructions('toggle 120,314 through 745,489')
    print('correct lighting instructions: ' + str(instruction[0]== -1))
    print('correct starting Coord: ' + str(instruction[1] == 120 and instruction[2] == 314))
    print('correct ending Coord: ' + str(instruction[3] == 745 and instruction[4] == 489))

def test3():
    matrix = part1.createMatrix(4,4)
    part1.executeInstruction(matrix, [1,0,0,0,3])
    print('first column was turned on: ' + str(isLit(matrix, 0,0,0,3) == 4))
    print('second column is still off: ' + str(isLit(matrix, 1,0,1,3) == 0))

def test4():
    matrix = part1.createMatrix(4, 4)
    part1.executeInstruction(matrix, [1,0,0,0,3])
    part1.executeInstruction(matrix, [-1,0,0,3,0])
    print('first column is turned on except origin: ' + str(isLit(matrix, 0,0,0,3) == 3))
    print('first row is turned on except origin: ' + str(isLit(matrix, 0,0,3,0) == 3))
    print(str(len(matrix)))

def isLit(matrix, x1, y1, x2, y2):
    count = 0
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            count += matrix[x][y]

    return count

    
group1()
group2()


