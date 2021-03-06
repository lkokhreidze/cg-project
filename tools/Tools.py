__author__ = 'suidov'

import numpy as np
from sklearn.preprocessing import normalize

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

def toCoordinates(filename, diff1, diff2):
    coords1 = []
    coords2 = []
    toAdd = np.zeros_like(diff1)
    for i in range(0, len(diff1)):
        for j in range(0,len(diff1[i])):
            if diff1[i][j] != 0 and diff2[i][j] != 0:
                    toAdd[i][j] = 1
    # here comes normalization

    result_array1 = normalize(diff1)
    result_array2 = normalize(diff2)

    for i in range(0,len(result_array1)):
        for j in range(0,len(result_array1[i])):
            if -0.001 < result_array1[i][j] < 0.001:
                toAdd[i][j] = 0

    for i in range(0,len(result_array2)):
        for j in range(0,len(result_array2[i])):
            if -0.001 < result_array2[i][j] < 0.001:
                toAdd[i][j] = 0

    for i in range(0, len(result_array1)):
        for j in range(0, len(result_array1[i])):
            if toAdd[i][j] == 1:
                    coords1.append(str(-(i - 84)) + "," + str(j - 179) + "," + format_float(result_array1[i][j]))
                    coords2.append(str(-(i - 84)) + "," + str(j - 179) + "," + format_float(result_array2[i][j]))
    toJSON(filename,coords1,coords2)


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


from1990 = toList("../datasource/glp90ag60.asc")
from2000 = toList("../datasource/glp00ag60.asc")
from2010 = toList("../datasource/glp10ag60.asc")

diff20002010 = getDifference(from2010, from2000)
diff19902000 = getDifference(from2000, from1990)

toCoordinates("../json/data.json", diff19902000, diff20002010)
