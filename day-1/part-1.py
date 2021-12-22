
inputFile = open('input.txt', 'r')
 
count = 0
lastLine = None
for line in inputFile.readlines():
    if lastLine is not None and int(line) > int(lastLine): 
        count += 1

    lastLine = line

print(count)