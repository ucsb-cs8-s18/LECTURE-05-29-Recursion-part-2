def addToEach(value,aList):
   if aList==[]:
      return []

   first = aList[0]
   rest = aList[1:]

   return [ first + value ]   + addToEach(value,rest)


def test_addToEach_1():
   assert addToEach(1,[3,4,5])==[4,5,6]

def test_addToEach_10():
   assert addToEach(10,[3,4,5])==[13,14,15]
