# .rstrip('\n')

inputFile = open('input.txt', 'r')
reportLines = list(map(lambda line: line.rstrip('\n'), inputFile.readlines()))

# print(reportLines)

numberOfReportLines = len(reportLines)
reportLineLength = len(reportLines[0])
gammaRate = ''

for i in range(0, reportLineLength):
    gammaRate += str(int(sum(map(lambda line: int(line[i]), reportLines)) > numberOfReportLines/2))

gammaRate = int(gammaRate, 2)
epsilonRate = gammaRate ^ int('1'*reportLineLength, 2)
print(gammaRate * epsilonRate)