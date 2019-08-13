class GetAllCombNew:
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
            raise StopIteration
        else:
            self.current += 1
            return self.__getitem__(self.current - 1)

if __name__ == '__main__':

    for i in GetAllCombNew(['AA','BB','CC'],1,4):
        print(i)
