class GetAllCombNew:
    def __init__(self, keys, minKeys, maxKeys):
        self.min = minKeys
        self.max = maxKeys
        self.keysLen =  len(keys)
        self.keys = keys
        self.current = 0

    def __getitem__(self, s):
        return 2

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.max:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

for i in GetAllCombNew(['a','b','c','d'],1,3):
    print(i)

