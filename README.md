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
The whole point of SmartBrute is to generate password lists using information about the target, in this step we'll declare some variables to hold that information. 

### 1.6 Stop
The whole point of SmartBrute is to generate password lists using information about the target, in this step we'll declare 

### 1.7 Running and output
Assuming all went well, the 

## 2. The different functions
