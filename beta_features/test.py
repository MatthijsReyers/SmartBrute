import time

def convertToBin(number:int, bits:int):
    out = [0 for i in range(bits)]
    for i in reversed(range(0,bits+1)):
        if number >= (2**i):
            number = number - (2**i)
            out[i] = 1
        if number == 0:
            break
    out.reverse()
    return out

def convertToBase(number:int, bits:int, base:int):
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
