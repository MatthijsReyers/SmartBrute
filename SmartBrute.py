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

class GetAllComb:
    def __init__(self, keys, minKeys, maxKeys):
        self.min = minKeys
        self.max = maxKeys
        self.keysLen =  len(keys)
        self.keys = keys
        self.current = 0
        self.len = 0
        for i in range(minKeys, maxKeys+1):
            self.len = self.len + (self.keysLen**i)

    def convertToBase(self, number:int, bits:int, base:int):
        out = [0 for i in range(bits)]
        for bit in reversed(range(bits)):
            for power in reversed(range(1,base)):
                testnum = power * (base**bit)
                if (number >= testnum):
                    number = number - testnum
                    out[bit] = power
                    break
        out.reverse()
        return out

    def __getitem__(self, itemIndex):
        # Figure out where the hell in the indexes we are.
        keyCount = 0
        stuffcounter = 0
        index = itemIndex

        for i in range(self.min, self.max+1):
            if itemIndex < (self.keysLen**i + stuffcounter):
                keyCount = i
                break
            else:
                index = index - (self.keysLen**i)
                stuffcounter = stuffcounter + (self.keysLen**i)

        # Do stuff
        keyIndexes = self.convertToBase(index, keyCount, self.keysLen)
        outKey = ''

        # Create string
        for ki in keyIndexes: outKey = outKey + self.keys[ki]
        return outKey

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.len:
            self.current = 0
            raise StopIteration
        else:
            self.current += 1
            return self.__getitem__(self.current - 1)

# class GetAllCombForEach:
#     def __init__(self, keys, toadd):
#         self.keys = keys
#         self.toadd = toadd
#         self.current = 0
#         self.len = len(keys) * len(toadd)

#         # OutKeys = []
#         # for key in keys:
#         #     for add in toadd:
#         #         OutKeys.append(key+add)
#         # return OutKeys

#     def __getitem__(self, itemIndex):
#         pass

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.current >= self.len:
#             self.current = 0
#             raise StopIteration
#         else:
#             self.current += 1
#             return self.__getitem__(self.current - 1)

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
