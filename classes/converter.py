def convertList(list):
    newList = []
    for l in list:
        newList.append(ord(l))
    return newList


def convertBack(list):
    newList = []
    for l in list:
        newList.append(chr(l))
    return newList
