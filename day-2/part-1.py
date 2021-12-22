def commandToTuple(command):
    [direction, value] = command.split(' ')
    return [direction, int(value)]

def directionValue(commands, direction):
    return sum(map(lambda command: command[1], filter(lambda command: command[0] == direction, commands)))

inputFile = open('input.txt', 'r')
commands = list(map(commandToTuple, inputFile.readlines()))

forwardValue = directionValue(commands, 'forward')
upValue = directionValue(commands, 'up')
downValue = directionValue(commands, 'down')

print(forwardValue * (downValue - upValue))