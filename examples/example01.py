from SmartBrute import *

SB = SmartBrute('example01.txt')
SB.setFilter({
    "max-length": 63,
    "min-length": 8,
    'forbidden-characters': ['@','#'],
    'echo-generated-passwords-in-terminal': True
})

NAMES = ['homer', 'marge', 'bart', 'lisa', 'maggie']
SURNAME = 'Simpson'

SB.add(GetAllTrueComb(NAMES))
SB.add(GetAllTrueComb(CapFirstChar(NAMES)))
SB.add([SURNAME+'Guest'])

SB.stop()
