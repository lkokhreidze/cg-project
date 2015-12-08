__author__ = 'suidov'

import numpy as np

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

    #normalizing data from 0 to 1
    '''
    input_array = np.array(diffList)
    if np.unique(input_array).shape[0] == 1:
        print ("Something's wrong here.")
        pass
    else:
        result_array=(input_array-np.min(input_array))/np.ptp(input_array)
        return result_array
    '''
    return diffList

def toCoordinates(filename, diff1, diff2):
    coords1 = []
    coords2 = []
    for i in range(0, len(diff1)):
        for j in range(0, len(diff1[i])):
            if diff1[i][j] != 0 and diff2[i][j] != 0:
                if diff1[i][j] > 0 and diff2[i][j] >0:
                    coords1.append(str(i  - 58) + "," + str(j - 180) + "," + format_float(diff1[i][j]))
                    coords2.append(str(i  - 58) + "," + str(j - 180) + "," + format_float(diff2[i][j]))
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





from1990 = toList("datasource/glp90ag60.asc")
from2000 = toList("datasource/glp00ag60.asc")
from2010 = toList("datasource/glp10ag60.asc")

diff20002010 = getDifference(from2010, from2000)
diff19902000 = getDifference(from2000, from1990)

toCoordinates("data.json", diff19902000, diff20002010)
