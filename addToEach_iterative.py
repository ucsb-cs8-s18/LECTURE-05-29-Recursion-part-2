def addToEach(value,aList):
   result = []
   for item in aList:
     result = result + [ item + value ]
   return result

#def addToEach(value,aList):
#   result = []
#   for item in aList:
#     result.append(item + value)
#   return result


def test_addToEach_1():
   assert addToEach(1,[3,4,5])==[4,5,6]

def test_addToEach_10():
   assert addToEach(10,[3,4,5])==[13,14,15]
