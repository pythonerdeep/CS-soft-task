digitsList = []
for i in range(4):
    str = input()
    digits = [int(x) for x in str.split(',')]
    digitsList.append(digits)

for i in range(len(digitsList)):
    rowNum = digitsList[i][0]
    colNum = digitsList[i][1]
    multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
    # print multilist

    val = 1
    for row in range(rowNum):
        for col in range(colNum):
            multilist[row][col] = val
            val += 1

    print(multilist)

for i in range(4):
    inputs = map(lambda x: int(x), input().split(','))
    ret = []
    for j in range(inputs[0]):
        ret.append(map(lambda x: x+j*inputs[1]+1, range(inputs[1])))
        print(ret)

input()
