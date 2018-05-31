

def runningSLen(listOfStrings):
    return runningSLenHelper(0,listOfStrings)

def runningSLenHelper(totalSoFar, listOfStrings):
    if listOfStrings==[]:
        return []

    first = listOfStrings[0]
    rest = listOfStrings[1:]

    return [ len(first) + totalSoFar ] + runningSLenHelper(totalSoFar + len(first), rest)


    
def test_1():
    assert runningSLen(["foo","bar","fum"])==[3,6,9]

def test_2():
    assert runningSLen(["A","BC","DEF","G"])==[1,3,6,7]

def test_3():
    assert runningSLen([])==[]
