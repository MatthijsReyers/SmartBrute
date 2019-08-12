def GenNumbers(minLen:int, maxLen:int, nums=[0,1,2,3,4,5,6,7,8,9]):
    OutKeys = []
    numsLen = len(nums)
    for looplen in range(minLen, maxLen + 1):
        counters = []
        print(looplen**numsLen)
        for i in range(looplen**numsLen):
            print(i)
    return OutKeys

GenNumbers(1,4)