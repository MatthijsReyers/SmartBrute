import groundtruth as gt
from SmartBrute import * 

testlist = ['java','is','garbage','and','you','know','it']

l1 = list(getAllComb(testlist))
l2 = gt.GetAllCombNoDoubles(testlist)

for i in range(len(l1)):
    x = l1[i]
    y = l2[i]
    if x != y:
        print('Wow that\'s wrong!',x,y) 

# assert list(getAllComb(testlist)) == gt.GetAllCombNoDoubles(testlist)
