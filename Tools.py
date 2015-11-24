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
            writeString += str(element) + ","
        writeString = writeString[:-1] + "\n"
        file.write(writeString)


i = float(0)

from1990 = toList("datasource/glp90ag60.asc")
from2000 = toList("datasource/glp00ag60.asc")
from2010 = toList("datasource/glp10ag60.asc")

diff20002010 = getDifference(from2010, from2000)
diff19902000 = getDifference(from2000, from1990)
toFormat("diff20002010.csv", diff20002010)
toFormat("diff19902000.csv", diff20002010)