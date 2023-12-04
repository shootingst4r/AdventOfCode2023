input = open("input3.txt","r")
inputlines = input.readlines()
input.close()

inputArray = []

def make_2d_Array(inputL):
    zsum = [[]]
    for i in inputL:
        zzsum = []
        for y in i:
            zzsum.append(y)
        zsum.append(zzsum)
    return zsum

arr = make_2d_Array(inputlines)
isnumarr = [[]]

for i in range(arr):
    for y in range(currLine):
        try:
            int(arr[i[y]])
            num
