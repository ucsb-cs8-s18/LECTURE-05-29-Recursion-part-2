

#def runningSum(aList):
#  result = []
#  total = 0
#  for item in aList:
#    total += item
#    result.append(total)
#  return result

def runningSum(aList):
   if type(aList)!=list:
      raise ValueError("should be a list")
   if aList==[]:
      return []
   if len(aList)==1:
      return aList
   first = aList[0]
   next = aList[1]
   rest = aList[2:]
   
   return [ first ] + runningSum( [first + next] + rest ) 
    


def test_runningSum_1():
  assert runningSum([16,3,4,10])==[16,19,23,33]

def test_runningSum_2():
  assert runningSum([10,5,10,5,-5,10])==[10,15,25,30,25,35]

def test_runningSum_3():
  assert runningSum([1,2,3,4,5])==[1,3,6,10,15]
