
inputFile = open('input.txt', 'r')
lines = inputFile.readlines()
 
count = 0
lastLine = None
for line in lines:
    if lastLine is not None and line > lastLine: 
        count += 1
    lastLine = line

print(count)