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

def toCoordinates(diffData):
    coords = []
    negatives = 0
    for i in range(0,len(diffData)):
        for j in range(0,len(diffData[i])):
            if diffData[i][j] != 0:
                if diffData[i][j] < 0:
                    negatives +=1
                coords.append(str(i * 1.0000000000008 - 58) + "," + str(j * 1.0000000000008 - 180) + "," + format_float(diffData[i][j]))
                #coords.append(str(i * 1.0000000000008 - 58) + "," + str(j * 1.0000000000008 - 180) + ", 1.0" )
    print (negatives)
    return coords

def format_float(value, precision=-1):
    if precision < 0:
        f = "%f" % value
    else:
        f = "%.*f" % (precision, value)

    p = f.partition(".")

    s = "".join((p[0], p[1], p[2][0], p[2][1:].rstrip("0")))

    return s

def toJSON(filename, diff1, diff2):
    file = open(filename, 'w')

    string1 = '["1990-2000",['
    for line in diff1:
        string1 = string1 + line + ","
    string1 = string1[:-1]
    string1 = string1 + "]],"

    string2 = '["2000-2010",['
    for line in diff2:
        string2 = string2 + line + ","
    string2 = string2[:-1]
    string2 = string2 + "]]"
    jsonString = "[" + string1 + string2 + "]"

    file.write(jsonString)



i = float(0)

from1990 = toList("datasource/glp90ag60.asc")
from2000 = toList("datasource/glp00ag60.asc")
from2010 = toList("datasource/glp10ag60.asc")

diff20002010 = getDifference(from2010, from2000)
diff19902000 = getDifference(from2000, from1990)
#toFormat("diff20002010.csv", diff20002010)
#toFormat("diff19902000.csv", diff20002010)

diff1 = toCoordinates(diff19902000)
diff2 = toCoordinates(diff20002010)

toJSON("data.json", diff1, diff2)