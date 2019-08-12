
from SmartBrute import *

SB = SmartBrute('example03.txt')

SB.setFilter({
    "max-length": 63,
    "min-length": 8,
    'echo-generated-passwords-in-terminal': False
})

def GetAllTrueCombEdit(keys):
    OutKeys = []
    for key in keys:
        OtherKeys = keys[:]
        OtherKeys.remove(key)
        OutKeys.append(key)
        if len(OtherKeys) == 1:
            OutKeys.append(key+OtherKeys[0])
        else:
            for rkey in GetAllTrueComb(OtherKeys):
                OutKeys.append(key+rkey)
    return OutKeys

years = GenYears(1900,2000)
nums = GetAllTrueCombEdit(['0','1','2','3','4','5','6','7','8','9'])
footballClubs = ['ajax','feyenoord','PSV','psv','AZ','az','fctwente','fcTwente','FCtwente','fcutrecht','fcUtrecht','FCutrecht']

# 'voetbal' + common years
voetbal = ['voetbal','Voetbal','VOETBAL','VoetBaL']
SB.add(GetAllCombForEach(voetbal,years))
SB.add(RepeatTillN(voetbal,4))
SB.add(RepeatTillN(voetbal,4))

# Football club + 'fan'/'lover'/etc.
words = ['fan','lover','gek','hooligan']
SB.add(GetAllCombForEach(footballClubs,words))
SB.add(GetAllCombForEach(CapFirstChar(footballClubs),words))
SB.add(GetAllCombForEach(footballClubs,CapFirstChar(words)))
SB.add(GetAllCombForEach(CapFirstChar(footballClubs),CapFirstChar(words)))

# 'voetbal' + 'fan'/'lover'/etc.
SB.add(GetAllCombForEach(voetbal,words))
SB.add(GetAllCombForEach(voetbal,CapFirstChar(words)))

# Football club + random number
SB.add(GetAllCombForEach(footballClubs,nums))
SB.add(GetAllCombForEach(CapFirstChar(footballClubs),nums))

# Random number + football club
SB.add(GetAllCombForEach(nums,footballClubs))
SB.add(GetAllCombForEach(nums,CapFirstChar(footballClubs)))

SB.stop()
