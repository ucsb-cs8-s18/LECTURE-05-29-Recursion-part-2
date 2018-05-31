
def sumList(intList):
    if intList==[]:
        return 0
    else:
        return intList[0] + sumList(intList[1:])


def sumList2(intList):
    if intList==[]:
        return 0

    first = intList[0]
    rest = intList[1:]
    return first + sumList2(rest)


def sumList3(intList):
    return sumListHelper(0,intList)

def sumListHelper(totalSoFar, intList):
    if intList==[]:
        return totalSoFar
    first = intList[0]
    rest = intList[1:]
    return sumListHelper(totalSoFar + first, rest)
