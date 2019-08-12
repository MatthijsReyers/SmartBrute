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

def convertToBase(num:int, bits:int, bas:int):

    for base in reversed(range(bas)):

        for i in reversed(range(bits)):

            print('base: ', base, '   i: ', i, '  value: ', (base+1)**(i+1))


# print(
#     convertToBase(300, 8, 4)
# )

# convertToBase(0, 4, 3)

# for i in range(0,251):
#     for bit in convertToBin(i, 8):
#         print(bit, end='')
#     print(' - ', i)
#     time.sleep(0.3)

for i in range()
