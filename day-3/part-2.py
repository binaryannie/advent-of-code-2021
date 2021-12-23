def findMostCommonValue(lines, digit):
    return str(int(sum(map(lambda line: int(line[digit]), lines)) >= len(lines)/2))

def findLeastCommonValue(lines, digit):
    return str(int(sum(map(lambda line: int(line[digit]), lines)) < len(lines)/2))

inputFile = open('input.txt', 'r')
reportLines = list(map(lambda line: line.rstrip('\n'), inputFile.readlines()))

numberOfReportLines = len(reportLines)
reportLineLength = len(reportLines[0])
oxygenGeneratorRating = None
co2ScrubberRating = None
possibleOgr = reportLines
possibleCsr = reportLines

for i in range(0, reportLineLength):
    mostCommonValue = findMostCommonValue(possibleOgr, i)
    possibleOgr = list(filter(lambda line: line[i] == mostCommonValue, possibleOgr))
    if(len(possibleOgr) == 1 and oxygenGeneratorRating is None):
        oxygenGeneratorRating = possibleOgr[0]

    leastCommonValue = findLeastCommonValue(possibleCsr, i)
    possibleCsr = list(filter(lambda line: line[i] == leastCommonValue, possibleCsr))
    if(len(possibleCsr) == 1 and co2ScrubberRating is None):
        co2ScrubberRating = possibleCsr[0]

    if(oxygenGeneratorRating is not None and co2ScrubberRating is not None):
        break


oxygenGeneratorRating = int(oxygenGeneratorRating, 2)
co2ScrubberRating = int(co2ScrubberRating, 2)
print(oxygenGeneratorRating * co2ScrubberRating)