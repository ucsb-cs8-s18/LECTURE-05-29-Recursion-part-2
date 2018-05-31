

def runningSLen(listOfStrings):

    result = []
    answer = 0
    for item in listOfStrings:
        answer += len(item)
        result.append(answer)
    return result      

def test_1():
    assert runningSLen(["foo","bar","fum"])==[3,6,9]

def test_2():
    assert runningSLen(["A","BC","DEF","G"])==[1,3,6,7]

def test_3():
    assert runningSLen([])==[]
