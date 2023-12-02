input = open("input1.txt","r")
inputlines = input.readlines()
input.close()

sum = 0 
zsum = ""
numbers = [0,1,2,3,4,5,6,7,8,9]
for i in range(len(inputlines)):
    inputlines[i] = inputlines[i].strip()

for i in range(len(inputlines)):
    inputlines[i] = inputlines[i].replace("zero", "z0o")
    inputlines[i] = inputlines[i].replace("one","o1e")
    inputlines[i] = inputlines[i].replace("two","t2o")
    inputlines[i] = inputlines[i].replace("three", "t3e")
    inputlines[i] = inputlines[i].replace("four","f4r")
    inputlines[i] = inputlines[i].replace("five","f5e")
    inputlines[i] = inputlines[i].replace("six","s6x")
    inputlines[i] = inputlines[i].replace("seven","s7n")
    inputlines[i] = inputlines[i].replace("eight","e8t")
    inputlines[i] = inputlines[i].replace("nine", "n9e")

for i in inputlines:
    for y in range(len(i)):
        try:
            int(i[y])
        except ValueError: 
            pass
        else:
            print(i[y])
            zsum=i[y]
            break
    
    for y in range(len(i)):
        try:
            int(i[len(i)-y-1])
        except ValueError: 
            pass
        else:
            print(i[len(i)-y-1])
            zsum+=i[len(i)-y-1]
            break
    sum += int(zsum)
        
print(sum)