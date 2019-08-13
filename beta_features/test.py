import time

def convertToBin(num:int, bits:int):
    number = num
    out = [0 for i in range(bits)]
    for i in reversed(range(0,bits+1)):
        if number >= (2**i):
            number = number - (2**i)
            out[i] = 1
        if number == 0:
            break
    out.reverse()
    return out

def convertToBase(num:int, bits:int, base:int):

    for bit in reversed(range(bits)):
        for power in reversed(range(base)):

            print( bit * (base**power) )


convertToBase(12,4,3)