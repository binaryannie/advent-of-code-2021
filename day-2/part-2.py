def commandToTuple(command):
    [direction, value] = command.split(' ')
    return [direction, int(value)]



inputFile = open('input.txt', 'r')
commands = list(map(commandToTuple, inputFile.readlines()))

depth = 0
aim = 0
horizontalPosition = 0
for [direction, value] in commands:
    if direction == 'forward':
        horizontalPosition += value 
        depth += aim * value
    if direction == 'down':
        aim += value
    if direction == 'up':
        aim -= value

print(horizontalPosition * depth)