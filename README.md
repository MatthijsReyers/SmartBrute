# SmartBrute - Bruteforce smarter with Python
Although password lists like 'rockyou.txt' are pretty good when bruteforcing several passwords from relatively unknown targets, in many situations you do know information about the target. And because many people (previously myself included) use passwords that are partially or entirely made out of publicly available information, I decided to create a simple tool in Python that can be used to generate password lists with information about a target.

If you have any suggestions on how to improve the code or want to share any generation scripts that you've come up with, please do contact me.

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

NAMES = ['Homer', 'Marge', 'Bart', 'Lisa', 'Maggie']
SURNAME = 'Simpson'

```

### 1.5 Adding passwords
Now that SmartBrute is properly set up it is time to start adding passwords to the list. 

### 1.6 Stop
The whole point of SmartBrute is to generate password lists using information about the target, in this step we'll declare 

### 1.7 Running and output
Assuming all went well, our example script should produce the output displayed below. If you experience any errors please ensure that the smartbrute.py file is located in the same directory as the script, and that you are using Python 3.

## 2. The different functions
SmartBrute includes a whole bunch of different functions to manipulate and generate arrays/lists of strings.

### GetAllComb(keys)
The GetAllComb function returns all possible combinations of the given keys/p based on the length of the 

| Example       | Output        |
| ------------- |:-------------:|
| ```ALFB = ['A','B','C','D']```<br>`GetAllComb(ALFB)` | `['ABCD', 'ABDC', 'ACBD', 'ACDB', 'ADBC', 'ADCB', 'BACD', 'BADC',`<br> `'BCAD', 'BCDA', 'BDAC', 'BDCA', 'CABD', 'CADB', 'CBAD', 'CBDA',`<br>`'CDAB', 'CDBA', 'DABC', 'DACB', 'DBAC', 'DBCA', 'DCAB', 'DCBA']` |

### GetAllTrueComb(keys)
The GetAllTrueComb function returns all possible combinations of the given keys/p based on the length of the 

| Example       | Output        |
| ------------- |:-------------:|
| ```ALFB = ['A','B','C','D']```<br>`GetAllComb(ALFB)` | `['ABCD', 'ABDC', 'ACBD', 'ACDB', 'ADBC', 'ADCB', 'BACD', 'BADC',`<br> `'BCAD', 'BCDA', 'BDAC', 'BDCA', 'CABD', 'CADB', 'CBAD', 'CBDA',`<br>`'CDAB', 'CDBA', 'DABC', 'DACB', 'DBAC', 'DBCA', 'DCAB', 'DCBA']` |

### GetFirstN(keys, N)
The GetFirstN function returns the first N characters of the given keys.

| Example       | Output        |
| ------------- |:-------------:|
| ```NAMES = ['Homer', 'Marge', 'Bart', 'Lisa', 'Maggie']```<br>```GetFirst(NAMES, 2)``` | `['Ho', 'Ma', 'Ba', 'Li', 'Ma']` |
