# SmartBrute - Bruteforce smarter with Python
Although password lists like 'rockyou.txt' are pretty good when bruteforcing several passwords from relatively unknown targets, in many situations you do know information about the target. And because many people (previously myself included) use passwords that are partially or entirely made out of publicly available information, I decided to create a simple tool in Python that can be used to generate password lists with information about a target.

If you have any suggestions on how to improve the code or want to share any of the scripts that you've come up with, please do contact me.

## 1. How to use SmartBrute
Followed underneath are the instructions for using the SmartBrute tool. If you have any problems feel free to ask for under the issues tab or on Twitter. The code used for these instructions can also be found in the 'example01.py' file in the repository.

### 1.1 Installation
To start you will need to download the smartbrute.py file and include it in the same directory as the script you want to use it in. You can then import the needed code by putting `from smartbrute import *` at the top of your script.
```
from smartbrute import *
```

### 1.2 Initialize the SmartBrute object
You can then make a SmartBrute object, which I will call `SB`. Please note that the `'example01.txt'` string is the name of the file you want to put the generated password list into and giving the name of a file that already exists will overwrite that file.
```
from smartbrute import *

SB = SmartBrute('example01.txt')
```

### 1.3 Filtering the generated passwords (optional step)
If you want to filter the generated passwords to, for example, not include any passwords longer then 63 characters (the maximum length of WPA2-PSK passwords), you can filter the generated passwords by calling the `setFilter` function with a dictonary. If you do **not** wish to filter the generated passwords in any way, you can skip this step.
```
from smartbrute import *

SB = SmartBrute('example01.txt')
SB.setFilter({
    "max-length": 63,
    "min-length": 8
})
```

### 1.4 Declaring variables
The whole point of SmartBrute is to generate password lists using information about the target, in this step we'll declare some variables to hold that information. Depending on what passwords you want to generate and what information you have you will have to decide what variables to create. For this example we will be trying to crack the wifi password of a imaginary family. 
```
from smartbrute import *

SB = SmartBrute('example01.txt')
SB.setFilter({
    "max-length": 63,
    "min-length": 8
})

NAMES = ['homer', 'marge', 'bart', 'lisa', 'maggie']
SURNAME = 'Simpson'
```

### 1.5 Adding and generating passwords
Now that SmartBrute is properly set up it is time to generate passwords and add them to the list to the outputfile. The basis for this is the `add()` method, which takes in an array/list of passwords and adds them to the output file.
For the first example I will use the `GetAllTrueComb()` function to generate all possible combinations that can be made with the names.
For the second example I will do the same thing as in the first example but this time  th
For the third exmaple I will simply Combine the surname with the string 'Guest', keep in mind that the `add()` method takes a array/list of strings so when you want to add only one string you should encase it with brackes (`[]`) to make it an array/list.
```
from new import *

SB = SmartBrute('example01.txt')
SB.setFilter({
    "max-length": 63,
    "min-length": 8
})

NAMES = ['homer', 'marge', 'bart', 'lisa', 'maggie']
SURNAME = 'Simpson'

SB.add(GetAllTrueComb(NAMES))
SB.add(GetAllTrueComb(CapFirstChar(NAMES)))
SB.add([SURNAME+'Guest'])
```

### 1.6 Stop
To tell the SmartBrute object that we are done generating passwords we need to call the `stop()` method. 
```
from new import *

SB = SmartBrute('example01.txt')
SB.setFilter({
    "max-length": 63,
    "min-length": 8
})

NAMES = ['homer', 'marge', 'bart', 'lisa', 'maggie']
SURNAME = 'Simpson'

SB.add(GetAllTrueComb(NAMES))
SB.add(GetAllTrueComb(CapFirstChar(NAMES)))
SB.add([SURNAME+'Guest'])

SB.stop()
```

### 1.7 Running and output
Assuming all went well, our example script should produce the output displayed below. If you experience any errors please ensure that the smartbrute.py file is located in the same directory as the script, and that you are using Python 3.
```
homermarge
homermargebart
homermargebartlisa
homermargebartlisamaggie
homermargebartmaggie
homermargebartmaggielisa
...
MaggieLisaBartHomer
MaggieLisaBartHomerMarge
MaggieLisaBartMarge
MaggieLisaBartMargeHomer
SimpsonGuest
```

## 2. The different functions
SmartBrute includes a bunch of different functions to manipulate and generate arrays/lists of strings.

### 2.1 GetAllComb(keys)
The GetAllComb function returns all possible ways in which the given keys/strings can be combined, while always using every given key, and never using a key twice. *PLEASE NOTE:* all of the keys this function outputs are kept in memory until they are written to the output file, which is why it is not recommended to use this function on extremely large arrays, or to nest this function multiple times.

| Example       | Output        |
| ------------- |:-------------:|
| ```ALFB = ['A','B','C','D']```<br>`GetAllComb(ALFB)` | `['ABCD', 'ABDC', 'ACBD', 'ACDB', 'ADBC', 'ADCB', 'BACD', 'BADC',`<br> `'BCAD', 'BCDA', 'BDAC', 'BDCA', 'CABD', 'CADB', 'CBAD', 'CBDA',`<br>`'CDAB', 'CDBA', 'DABC', 'DACB', 'DBAC', 'DBCA', 'DCAB', 'DCBA']` |

### 2.2 GetAllTrueComb(keys)
The GetAllTrueComb function returns all possible ways in which the given keys/strings can be combined, while never using the same key twice, but not necessarily using every key for every combination. *PLEASE NOTE:* all of the keys this function outputs are kept in memory until they are written to the output file, which is why it is not recommended to use this function on extremely large arrays, or to nest this function multiple times.

| Example       | Output        |
| ------------- |:-------------:|
| ```ALFB = ['A','B','C','D']```<br>`GetAllComb(ALFB)` | `['A', 'AB', 'ABC', 'AC', 'ACB',`<br>`'B', 'BA', 'BAC', 'BC', 'BCA',`<br>` 'C', 'CA', 'CAB', 'CB', 'CBA']` |

### GetFirstN(keys, N)
The GetFirstN function returns the first N characters of the given keys.

| Example       | Output        |
| ------------- |:-------------:|
| ```NAMES = ['Homer', 'Marge', 'Bart', 'Lisa', 'Maggie']```<br>```GetFirst(NAMES, 2)``` | `['Ho', 'Ma', 'Ba', 'Li', 'Ma']` |
