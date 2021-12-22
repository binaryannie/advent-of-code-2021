def windowed(list, windowSize):
    for i in range(len(list) - windowSize + 1):
        yield list[i:i+windowSize]

inputFile = open('input.txt', 'r')
depths = list(map(int, inputFile.readlines()))

count = 0
depthWindows = list(windowed(depths, 3))
lastWindowSum = None
for window in depthWindows:
    currentWindowSum = sum(window)
    if lastWindowSum is not None and currentWindowSum > lastWindowSum:
        count += 1

    lastWindowSum = currentWindowSum

print(count)
