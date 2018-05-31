

def makeEvenLength(alist):
    result = []
    for item in alist:
        if len(item)%2 == 0:
           result.append(  item    )
        else:
           result.append( item + " ")
           
    return result

def test_makeEvenLength_1():

  assert makeEvenLength(["UCSB","UCI","Chico State"])==["UCSB","UCI ","Chico State "]

                             
