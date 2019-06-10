#!/usr/bin/python3

class SmartBrute():

    def __init__(self, OutputFile):
        self.OutFile = open(OutputFile, "w+")
        self.FilterOut = False

    def setFilter(self, Rules):
        pass
    
    def filter(self, pws):
        pass

    def add(self, keys):
        for key in keys:
            if self.FilterOut:
                # if len(key) > LengthMin and len(key) < LengthMax:
                #     self.OutFile.write(key+"\n")
                #     print(key)
                pass
            else:
                self.OutFile.write(key+"\n")
                print(key)

    def stop(self):
        self.OutFile.close()
        # Exit application to prevent anymore calling of add() function.
        exit(0)

def GetAllComb(keys):
    OutKeys = []
    for key in keys:
        OtherKeys = keys[:]
        OtherKeys.remove(key)
        if len(OtherKeys) == 1:
            OutKeys.append(key+OtherKeys[0])
        else:
            for rkey in GetAllComb(OtherKeys):
                OutKeys.append(key+rkey)
    return OutKeys

def GetAllTrueComb(keys):
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

def GetAllCombForEach(keys, toadd):
    OutKeys = []
    for key in keys:
        for add in toadd:
            OutKeys.append(key+add)
    return OutKeys

def GetFirstN(keys, n):
    OutKeys = []
    for key in keys:
        OutKeys.append(key[:n])
    return OutKeys

def GenYears(start, stop):
    OutKeys = []
    for year in range(start, stop):
        OutKeys.append(str(year))
    print('done generating years')
    return OutKeys

def AddString(keys, string):
    OutKeys = []
    for key in keys:
        OutKeys.append(key+string)
    return OutKeys

def AddForEach(keys, strings):
    OutKeys = []
    for string in strings:
        for key in keys:
            OutKeys.append(key+string)
    return OutKeys

def ReplaceString(keys, replace, new):
    OutKeys = []
    for key in keys:
        out = key.replace(replace, new)
        OutKeys.append(out)
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
