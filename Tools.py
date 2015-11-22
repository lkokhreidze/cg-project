__author__ = 'suidov'


def toList(filename):
    popList = []
    with open(filename) as file:
        for line in file:
            strList = line.split()
            floatList = []
            for element in strList:
                floatList.append(float(element))
            popList.append(floatList)
    return popList

def getDifference(newData, oldData):
    assert len(newData) == len(oldData)
    diffList = []

    for i in range(0, len(newData)):
        list = []
        for j in range(0, len(newData[i])):
            element = newData[i][j] - oldData[i][j]
            list.append(element)
        diffList.append(list)

    return diffList

def toFormat(filename, diffData):
    file = open(filename, 'w')

    for line in diffData:
        writeString = ""
        for element in line:
            writeString += str(element) + " "
        writeString = writeString[:-1] + "\n"
        file.write(writeString)


i = float(0)

older = toList("2000.asc")
newer = toList("2010.asc")

diff = getDifference(newer, older)
toFormat("diff20002010.asc", diff)