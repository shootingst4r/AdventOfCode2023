input = open("input2.txt","r")
inputlines = input.readlines()
input.close()

for textLine in inputlines:
    splitLine = textLine.split(" ")
    gameId = splitLine[1][:-1]