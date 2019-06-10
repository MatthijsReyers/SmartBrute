# SmartBrute - Bruteforce smarter with Python
A python library/script for generating passworld lists using information about the target.

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

### 1.3 Filtering the generated passwords
If you want to filter the generated passwords to, for example, not generate any passwords longer then 

## 2. The different functions
