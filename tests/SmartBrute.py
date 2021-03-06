#!/usr/bin/python3

class SmartList():
    def __init__(self, OutputFile:str):
        self.OutFile = open(OutputFile, 'w+')
        self.maxLength = -1
        self.minLength = -1
        self.forbidenChars = []
        self.echoKeys = False

    def __enter__(self):
        pass

    def __exit__(self, *unused) -> None:
        self.OutFile.close()

    def setFilter(self, Rules:dict) -> None:
        # Set maximum length if given.
        try: self.maxLength = int(Rules['max-length'])
        except: self.maxLength = 0

        # Set minimum length if given.
        try: self.minLength = int(Rules['min-length'])
        except: self.minLength = 0

        # Set forbidden characters if given.
        try: self.forbidenChars = Rules['forbidden-characters']
        except: self.forbidenChars = []

        # Set whether to print generated passwords to terminal.
        try: self.echoKeys = bool(Rules['echo-generated-passwords-in-terminal'])
        except: self.echoKeys = False

    def addKeys(self, keys:list) -> None:
        for key in keys:
            self.addKey(key)

    def addKey(self, key:str) -> None:
        # Max length check.
        if self.xaxLength and (len(key) > self.maxLength): 
            return
        
        # Min Length check.
        if self.minLength and (len(key) < self.minLength): 
            return

        # Forbidden characters check.
        if self.forbidenChars and any(char in key for char in self.forbidenChars):
            return

        # Print keys check
        if self.echoKeys: 
            print(key)

        # Actually add the key to output file.
        self.OutFile.write(key+'\n')

    def close(self) -> None:
        self.__exit__()

class KeyGenerator():
    def __init__(self):
        pass

class getAllComb(KeyGenerator):
    def __init__(self, keys, minKeys=1, maxKeys=0):
        self.min = minKeys
        self.max = maxKeys or len(keys)
        self.keysLen =  len(keys)
        self.keys = keys
        self.current = 0
        self.len = 0
        for i in range(self.min, self.max+1):
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

class genYears(KeyGenerator):
    def __init__(self, start:int, stop:int):
        self.start = start
        self.stop = stop + 1
        self.current = 0

    def __getitem__(self, i:int) -> str:
        return str(self.start+i)

    def __iter__(self):
        return self

    def __next__(self) -> str:
        self.current += 1
        if (self.current > self.stop - self.start):
            self.current = 0
            raise StopIteration
        else:
            return self.__getitem__(self.current-1)

