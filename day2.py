input = open("input2.txt","r")
inputlines = input.readlines()
input.close()

result = 0 

for textLine in inputlines:
    splitLine = textLine.split(" ")
    gameId = int(splitLine[1][:-1])
    colors = splitLine[2:]
    colors = "".join(colors).lower().replace("\n", "")
    pullList = colors.split(";")
    highestRed = 0
    hightestGreen = 0 
    hightestBlue = 0 
    for currPull in pullList:
        for i in range(len(currPull)):
            nom = currPull.split(",")
            for y in nom:
                if "red" in y:
                    num = int(y[:-3])
                    if num > highestRed:
                        highestRed = num
                    pass
                elif "green" in y:
                    num = int(y[:-5])
                    if num > hightestGreen:
                        hightestGreen = num
                    pass
                elif "blue" in y:
                    num = int(y[:-4])
                    if num > hightestBlue:
                        hightestBlue = num
                    pass
    power = highestRed*hightestGreen*hightestBlue
    result += power

print(result)