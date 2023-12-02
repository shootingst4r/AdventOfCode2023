input = open("input2.txt","r")
inputlines = input.readlines()
input.close()
redMax = 12
greenMax = 13
blueMax = 14

result = 0 

for textLine in inputlines:
    splitLine = textLine.split(" ")
    gameId = int(splitLine[1][:-1])
    colors = splitLine[2:]
    colors = "".join(colors).lower().replace("\n", "")
    pullList = colors.split(";")
    itdobeworking = True
    for currPull in pullList:
        for i in range(len(currPull)):
            nom = currPull.split(",")
            for y in nom:
                if "red" in y:
                    num = int(y[:-3])
                    if num > redMax:
                        itdobeworking = False
                    pass
                elif "green" in y:
                    num = int(y[:-5])
                    if num > greenMax:
                        itdobeworking = False
                    pass
                elif "blue" in y:
                    num = int(y[:-4])
                    if num > blueMax:
                        itdobeworking = False
                    pass
    if itdobeworking == True:
        result += gameId

print(result)