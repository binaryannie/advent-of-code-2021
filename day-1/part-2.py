def windowed(list, windowSize):
    for i in range(len(list) - windowSize + 1):
        yield list[i:i+windowSize]

inputFile = open('input.txt', 'r')
lines = list(map(int, inputFile.readlines()))

count = 0
windows = list(windowed(lines, 3))
lastWindowSum = None
for window in windows:
    currentWindowSum = sum(window)
    if lastWindowSum is not None and currentWindowSum > lastWindowSum:
        count += 1

    lastWindowSum = currentWindowSum

print(count)
