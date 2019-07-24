#!/usr/bin/python3

class SmartBrute():

    def __init__(self, OutputFile):
        self.OutFile = open(OutputFile, 'w+')
        self.MaxLength = [False, 0]
        self.MinLength = [False, 0]
        self.ForbidChars = [False, []]
        self.PrintPass = True

    def setFilter(self, Rules):
        # Set maximum length if given.
        try: self.MaxLength = [True, int(Rules['max-length'])]
        except: self.MaxLength = [False, 0]

        # Set minimum length if given.
        try: self.MinLength = [True, int(Rules['min-length'])]
        except: self.MinLength = [False, 0]

        # Set forbidden characters if given.
        try: self.ForbidChars = [True, Rules['forbidden-characters']]
        except: self.ForbidChars = [False, []]

        # Set whether to print generated passwords to terminal.
        try: self.PrintPass = bool(Rules['echo-generated-passwords-in-terminal'])
        except: self.PrintPass = True

    def add(self, keys):
        for key in keys:
            # Max length check.
            if (self.MaxLength[0] and len(key) > self.MaxLength[1]): continue
            
            # Min Length check.
            if (self.MinLength[0] and len(key) < self.MinLength[1]): continue

            # Forbidden characters check.
            if self.ForbidChars[0]:
                dirtyCheck = True
                for char in self.ForbidChars[1]:
                    if char in key:
                        break
                else: 
                    dirtyCheck = False
                if dirtyCheck: continue

            # Print keys check
            if self.PrintPass: print(key)

            # Actually add the key to output file.
            self.OutFile.write(key+'\n')

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
            for more in range(step+1):
                AddKey = AddKey+key
            OutKeys.append(AddKey)
    return OutKeys

def GenYears(start, stop):
    OutKeys = []
    for year in range(int(start), int(stop)+1):
        OutKeys.append(str(year))
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
