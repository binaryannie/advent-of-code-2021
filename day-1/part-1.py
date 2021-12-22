inputFile = open('input.txt', 'r')
depths = list(map(int, inputFile.readlines()))
 
count = 0
lastDepth = None
for depth in depths:
    if lastDepth is not None and depth > lastDepth:
        count += 1

    lastDepth = depth

print(count)