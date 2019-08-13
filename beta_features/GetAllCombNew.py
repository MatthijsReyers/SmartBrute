class GetAllCombNew:
    def __init__(self, keys, minKeys, maxKeys):
        self.min = minKeys
        self.max = maxKeys
        self.keysLen =  len(keys)
        self.keys = keys
        self.current = 0
        self.len = 0
        for i in range(minKeys, maxKeys+1):
            self.len = self.len + (i**self.keysLen)

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

    def __getitem__(self, s):
        return 2

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.len:
            raise StopIteration
        else:
            self.current += 1
            return self.__getitem__(self.current)

if __name__ == '__main__':

    for test in GetAllCombNew(['test','wow'],4,4):

        print(test)
