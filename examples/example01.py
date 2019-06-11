from smartbrute import *

SB = SmartBrute('example01.txt')
SB.setFilter({
    "max-length": 63,
    "min-length": 8
})

NAMES = ['bart', 'lisa', 'maggie']
YEARS = ['2000', '2001', '2002']
GetAllCombForEach(NAMES,YEARS)

SB.stop()
