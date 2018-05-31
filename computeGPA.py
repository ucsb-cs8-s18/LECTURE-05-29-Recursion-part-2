import pytest

grade2Number = {
    'A' : 4.0,
    'A-': 3.7,
    'B+': 3.3,
    'B': 3.0,
    'B-': 2.7,
    'C' : 2.0
    }

def computeGPA(courseList):
    qualityPoints = 0
    units = 0

    for course in courseList:
        units += course['units']
        qualityPoints += course['units'] *  grade2Number[ course['grade']  ] 

    return qualityPoints / units


def test_1():
    assert computeGPA( [  {"units": 4, "grade": "A" , "course": "CMPSC 8" }, 
                          {"units": 5, "grade": "B+" , "course": "MATH 8" },
                          {"units": 4, "grade": "A-" , "course": "MATH 6B" } ])  == pytest.approx(3.63846153846)

def test_2():
    assert computeGPA( [  {"units": 4, "grade": "A" , "course": "CMPSC 8" },
                          {"units": 5, "grade": "A" , "course": "MATH 8" },
                          {"units": 4, "grade": "A" , "course": "MATH 6B" } ] ) == pytest.approx(4.00)

def test_3():
    assert computeGPA( [  {"units": 4, "grade": "C" , "course": "CMPSC 8" },
                          {"units": 5, "grade": "C" , "course": "MATH 8" },
                          {"units": 4, "grade": "C" , "course": "MATH 6B" } ])  == pytest.approx(2.00)
