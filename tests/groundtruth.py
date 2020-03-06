

def GetAllCombNoDoubles(keys):
    OutKeys = []
    for key in keys:
        OtherKeys = keys[:]
        OtherKeys.remove(key)
        if len(OtherKeys) == 1:
            OutKeys.append(key+OtherKeys[0])
        else:
            for rkey in GetAllCombNoDoubles(OtherKeys):
                OutKeys.append(key+rkey)
    return OutKeys

def GetAllCombForEach(keys, toadd):
    OutKeys = []
    if type(toadd) == type([]):
        for key in keys:
            for add in toadd:
                OutKeys.append(key+add)
    else:
        for add in toadd:
            for key in keys:
                OutKeys.append(key+add)
    return OutKeys

def GetFirstN(keys, n):
    OutKeys = []
    for key in keys:
        OutKeys.append(key[:n])
    return OutKeys

def RepeatN(keys, N):
    OutKeys = []
    for key in keys:
        AddKey = ''
        for step in range(N):
            AddKey = AddKey+key
        OutKeys.append(AddKey)
    return OutKeys

def RepeatTillN(keys, N):
    OutKeys = []
    for key in keys:
        for step in range(N):
            AddKey = ''
            for step2 in range(step+1):
                AddKey = AddKey+key
            OutKeys.append(AddKey)
    return OutKeys


def AddString(keys, string):
    OutKeys = []
    for key in keys:
        OutKeys.append(key+string)
    return OutKeys

def AddForEach(keys1, keys2):
    OutKeys = []
    for key in keys1:
        for add in keys2:
            OutKeys.append(key+add)
    return OutKeys

def ReplaceString(keys, replace, new):
    OutKeys = []
    for key in keys:
        out = key.replace(replace, new)
        OutKeys.append(out)
    return OutKeys

def RemoveDoubles(keys):
    OutKeys = []
    for key in keys:
        if key not in OutKeys:
            OutKeys.append(key)
    return OutKeys

def CapFirstChar(keys):
    OutKeys = []
    for key in keys:
        out = str.capitalize(key)
        OutKeys.append(out)
    return OutKeys

def CapAllChar(keys):
    OutKeys = []
    for key in keys:
        OutKeys.append(key.upper())
    return OutKeys
