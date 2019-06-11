from smartbrute import *

# Variables
NAMES = ['homer', 'marge', 'bart', 'lisa', 'maggie']
SURNAME = 'simpson'
CITY = "springfield"
StreetName = "queekhoven"
StreetNr = "125"
SSID = "wifiname"

SB = SmartBrute('example02.txt')

# All possible compinations of names
SB.add(GetAllTrueComb(NAMES))
SB.add(GetAllTrueComb(CapFirstChar(NAMES)))

# All possible compinations of names + surname behind it.
SB.add(AddString(GetAllTrueComb(NAMES),SURNAME))
SB.add(AddString(GetAllTrueComb(CapFirstChar(NAMES)),str.capitalize(SURNAME)))

# All possible compinations of names with surname repeated in between.
SB.add(GetAllTrueComb(AddString(NAMES,SURNAME)))
SB.add(GetAllTrueComb(AddString(CapFirstChar(NAMES),str.capitalize(SURNAME))))

# Possible combinations of address info.
SB.add(GetAllTrueComb([
    SURNAME,
    CITY,
    StreetName,
    StreetNr
]))
SB.add(GetAllTrueComb([
    str.capitalize(SURNAME),
    str.capitalize(CITY),
    str.capitalize(StreetName),
    StreetNr
]))

# Trying some stuff with "household"
SB.add([SURNAME+"household"])
SB.add([SURNAME+"household"+StreetName])
SB.add([SURNAME+"household"+StreetName+StreetNr])
SB.add([str.capitalize(SURNAME)+"Household"])
SB.add([str.capitalize(SURNAME)+"Household"+str.capitalize(StreetName)])
SB.add([str.capitalize(SURNAME)+"Household"+str.capitalize(StreetName)+StreetNr])

# Trying some stuff with "guest"
SB.add([SURNAME+"guest"])
SB.add([SURNAME+"guest"+StreetName])
SB.add([SURNAME+"guest"+StreetName+StreetNr])
SB.add([str.capitalize(SURNAME)+"Guest"])
SB.add([str.capitalize(SURNAME)+"Guest"+str.capitalize(StreetName)])
SB.add([str.capitalize(SURNAME)+"Guest"+str.capitalize(StreetName)+StreetNr])

# Trying some stuff with 'is cool'
SB.add(AddString(NAMES,' is cool'))
SB.add(AddString(CapFirstChar(NAMES),' is cool'))
SB.add(ReplaceString(ReplaceString(ReplaceString(AddString(NAMES,' is cool'),'o','0'),'i','1'),'e','3'))
SB.add(ReplaceString(ReplaceString(ReplaceString(AddString(CapFirstChar(NAMES),' is cool'),'o','0'),'i','1'),'e','3'))

# Generate name + a year between 1970 and 2019
SB.add(GetAllCombForEach(NAMES,GenYears(1970,2019)))

# Generate address + a year between 1970 and 2019
SB.add(GetAllCombForEach([StreetName],GenYears(1970,2019)))
SB.add(GetAllCombForEach([StreetName+StreetNr],GenYears(1970,2019)))
SB.add(GetAllCombForEach([CITY+StreetName+StreetNr],GenYears(1970,2019)))
SB.add(GetAllCombForEach([StreetName+StreetNr+CITY],GenYears(1970,2019)))
SB.add(GetAllCombForEach([str.capitalize(StreetName)],GenYears(1970,2019)))
SB.add(GetAllCombForEach([str.capitalize(StreetName)+StreetNr],GenYears(1970,2019)))
SB.add(GetAllCombForEach([str.capitalize(CITY)+str.capitalize(StreetName)+StreetNr],GenYears(1970,2019)))
SB.add(GetAllCombForEach([str.capitalize(StreetName)+StreetNr+str.capitalize(CITY)],GenYears(1970,2019)))

# All possible compinations of names with a year behind it.
SB.add(GetAllCombForEach(GetAllTrueComb(NAMES),GenYears(1970,2019)))
SB.add(GetAllCombForEach(GetAllTrueComb(CapFirstChar(NAMES)),GenYears(1970,2019)))

# All possible compinations of names with some numbers inbetween.
SB.add(GetAllTrueComb(AddString(NAMES,'12')))
SB.add(GetAllTrueComb(AddString(NAMES,'123')))
SB.add(GetAllTrueComb(AddString(NAMES,'1234')))
SB.add(GetAllTrueComb(AddString(NAMES,'12345')))
SB.add(GetAllTrueComb(CapFirstChar(AddString(NAMES,'12'))))
SB.add(GetAllTrueComb(CapFirstChar(AddString(NAMES,'123'))))
SB.add(GetAllTrueComb(CapFirstChar(AddString(NAMES,'1234'))))
SB.add(GetAllTrueComb(CapFirstChar(AddString(NAMES,'12345'))))

SB.stop()
